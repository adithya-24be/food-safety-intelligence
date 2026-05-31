from db import cursor
import re

CRITICAL_SIGNALS = [
    "food poisoning",
    "undercooked chicken",
    "raw chicken",
    "mold",
    "expired food"
]

HIGH_RISK_SIGNALS = [
    "bad smell",
    "rotten food",
    "slimy vegetables",
    "hair in food",
    "foreign object",
    "spoilage",
    "potential microbial growth",
    "contamination"
]


def extract_detected_signals(gemini_text):

    match = re.search(
        r"Detected Signals:\s*(.*?)\n\nSeverity Level:",
        gemini_text,
        re.DOTALL | re.IGNORECASE
    )

    if not match:
        return []

    signal_text = match.group(1)

    return [
        x.strip().lower()
        for x in signal_text.split(",")
        if x.strip()
    ]


def calculate_score(gemini_text):

    score = 100

    detected = extract_detected_signals(
        gemini_text
    )

    for signal in detected:

        cursor.execute(
            """
            SELECT score_impact
            FROM HygieneRules
            WHERE signal_name = %s
            """,
            (signal,)
        )

        result = cursor.fetchone()

        if result:

            score += result[0]

    for signal in detected:

        if signal in CRITICAL_SIGNALS:

            score = min(score, 25)

        elif signal in HIGH_RISK_SIGNALS:

            score = min(score, 50)

    if "Severity Level:\nHigh" in gemini_text:

        score = min(score, 40)

    elif "Severity Level:\nMedium" in gemini_text:

        score = min(score, 70)

    score = max(
        0,
        min(score, 100)
    )

    return score, detected