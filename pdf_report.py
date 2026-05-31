from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    filename,
    restaurant,
    score,
    risk,
    issues,
    analysis
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Food Safety Intelligence Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"<b>Restaurant:</b> {restaurant}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Confidence Score:</b> {score}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Risk Level:</b> {risk}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Detected Issues</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            issues,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>AI Assessment</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            analysis,
            styles["BodyText"]
        )
    )

    doc.build(content)