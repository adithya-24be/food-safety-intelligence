from risk_index import get_risk_penalty


def calculate_confidence(
    food_score,
    rating,
    total_orders,
    complaints,
    refunds,
    review_bonus,
    restaurant_name
):

    BASE_SCORE = 80

    score = BASE_SCORE

    # -------------------------
    # Food Risk Impact
    # -------------------------
    food_penalty = 100 - food_score
    score -= food_penalty

    # -------------------------
    # Rating Impact
    # -------------------------
    rating_score = 0

    if rating >= 4.5:
        rating_score = 10
    elif rating >= 4.0:
        rating_score = 5
    elif rating >= 3.5:
        rating_score = 0
    else:
        rating_score = -15

    score += rating_score

    # -------------------------
    # Complaint Impact
    # -------------------------
    complaint_rate = (
        complaints / total_orders
    ) * 100

    if complaint_rate < 1:
        complaint_score = 10
    elif complaint_rate < 2:
        complaint_score = 5
    elif complaint_rate < 5:
        complaint_score = 0
    elif complaint_rate < 10:
        complaint_score = -10
    else:
        complaint_score = -20

    score += complaint_score

    # -------------------------
    # Refund Impact
    # -------------------------
    refund_rate = (
        refunds / total_orders
    ) * 100

    if refund_rate < 1:
        refund_score = 5
    elif refund_rate < 3:
        refund_score = 0
    elif refund_rate < 5:
        refund_score = -5
    else:
        refund_score = -10

    score += refund_score

    # -------------------------
    # Review Impact
    # -------------------------
    score += review_bonus

    # -------------------------
    # Incident History Impact
    # -------------------------
    incident_penalty = get_risk_penalty(
        restaurant_name
    )

    score += incident_penalty

    # -------------------------
    # Final Clamp
    # -------------------------
    score = max(
        0,
        min(score, 100)
    )

    return {
        "final_score": round(score),

        "food_penalty": food_penalty,

        "rating_score": rating_score,

        "complaint_score": complaint_score,

        "refund_score": refund_score,

        "review_score": review_bonus,

        "incident_penalty": incident_penalty,

        "complaint_rate": round(
            complaint_rate, 2
        ),

        "refund_rate": round(
            refund_rate, 2
        )
    }