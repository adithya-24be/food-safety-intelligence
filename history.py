from db import conn, cursor


def save_analysis(
    restaurant_name,
    user_description,
    detected_signals,
    confidence_score,
    risk_level
):

    cursor.execute(
        """
        INSERT INTO AnalysisHistory
        (
            restaurant_name,
            user_description,
            detected_signals,
            confidence_score,
            risk_level
        )
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            restaurant_name,
            user_description,
            detected_signals,
            confidence_score,
            risk_level
        )
    )

    conn.commit()


def get_analysis_history():

    cursor.execute(
        """
        SELECT
            restaurant_name,
            user_description,
            detected_signals,
            confidence_score,
            risk_level
        FROM AnalysisHistory
        ORDER BY analysis_id DESC
        LIMIT 50
        """
    )

    return cursor.fetchall()