from gemini_helper import extract_signals

from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    send_file
)

from scoring import calculate_score
from restaurant_score import get_restaurant_metrics
from review_score import get_review_score
from confidence_engine import calculate_confidence

from history import (
    save_analysis,
    get_analysis_history
)

from incident import save_incidents
from dashboard import get_dashboard

from pdf_report import generate_pdf

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    data = get_dashboard()

    return render_template(
        "dashboard.html",
        issue=data["issue"],
        restaurant=data["restaurant"],
        total_incidents=data["total_incidents"],
        recent=data["recent"],
        restaurant_chart=data["restaurant_chart"],
        avg_confidence=data["avg_confidence"],
        risk_distribution=data["risk_distribution"],
        confidence_trend=data["confidence_trend"]
    )


@app.route("/history")
def history_page():

    history = get_analysis_history()

    return render_template(
        "history.html",
        history=history
    )


@app.route("/download-report")
def download_report():

    generate_pdf(
        "food_report.pdf",
        "Demo Restaurant",
        85,
        "Minor Concerns",
        "Bad smell detected",
        "Food should be consumed with caution."
    )

    return send_file(
        "food_report.pdf",
        as_attachment=True
    )


@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.json

        user_message = data["message"]
        restaurant_name = data["restaurant"]

        signals_text = extract_signals(
            user_message
        )

        print("Gemini Output:", signals_text)

        food_score, detected = calculate_score(
            signals_text
        )

        metrics = get_restaurant_metrics(
            restaurant_name
        )

        if not metrics:

            return jsonify({
                "error": "Restaurant not found"
            })

        rating, total_orders, complaints, refunds = metrics

        review_bonus = get_review_score(
            restaurant_name
        )

        confidence = calculate_confidence(
            food_score,
            rating,
            total_orders,
            complaints,
            refunds,
            review_bonus,
            restaurant_name
        )

        final_score = confidence["final_score"]

        if final_score >= 85:
            risk = "High Confidence"

        elif final_score >= 70:
            risk = "Minor Concerns"

        elif final_score >= 50:
            risk = "Consume With Caution"

        elif final_score >= 25:
            risk = "High Risk"

        else:
            risk = "Do Not Consume"

        save_analysis(
            restaurant_name,
            user_message,
            ", ".join(detected),
            final_score,
            risk
        )

        save_incidents(
            restaurant_name,
            detected
        )

        return jsonify({

            "score": final_score,

            "restaurant": restaurant_name,

            "risk": risk,

            "issues": detected,

            "analysis": signals_text,

            "metrics": {

                "rating": rating,
                "orders": total_orders,
                "complaints": complaints,
                "refunds": refunds

            },

            "breakdown": {

                "food_penalty":
                confidence["food_penalty"],

                "rating_score":
                confidence["rating_score"],

                "review_score":
                confidence["review_score"],

                "complaint_score":
                confidence["complaint_score"],

                "refund_score":
                confidence["refund_score"],

                "incident_penalty":
                confidence["incident_penalty"]

            }

        })

    except Exception as e:

        print("ERROR:", str(e))

        return jsonify({

            "error": str(e)

        })


if __name__ == "__main__":
    app.run(debug=True)