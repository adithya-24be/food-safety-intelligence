from db import cursor


def most_common_issue():

    cursor.execute(
        """
        SELECT
            issue_type,
            COUNT(*) as total
        FROM RestaurantIncidents
        GROUP BY issue_type
        ORDER BY total DESC
        LIMIT 1
        """
    )

    return cursor.fetchone()


def worst_restaurant():

    cursor.execute(
        """
        SELECT
            restaurant_name,
            COUNT(*) as total
        FROM RestaurantIncidents
        GROUP BY restaurant_name
        ORDER BY total DESC
        LIMIT 1
        """
    )

    return cursor.fetchone()


def total_incidents():

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM RestaurantIncidents
        """
    )

    return cursor.fetchone()[0]


def incidents_by_restaurant():

    cursor.execute(
        """
        SELECT
            restaurant_name,
            COUNT(*) as total
        FROM RestaurantIncidents
        GROUP BY restaurant_name
        ORDER BY total DESC
        """
    )

    return cursor.fetchall()


def recent_analyses():

    cursor.execute(
        """
        SELECT
            restaurant_name,
            confidence_score,
            risk_level
        FROM AnalysisHistory
        ORDER BY analysis_id DESC
        LIMIT 5
        """
    )

    return cursor.fetchall()
def average_confidence():

    cursor.execute(
        """
        SELECT AVG(confidence_score)
        FROM AnalysisHistory
        """
    )

    result = cursor.fetchone()[0]

    if result:
        return round(result, 2)

    return 0
def risk_distribution():

    cursor.execute(
        """
        SELECT
            risk_level,
            COUNT(*) as total
        FROM AnalysisHistory
        GROUP BY risk_level
        """
    )

    return cursor.fetchall()
def risk_distribution():

    cursor.execute(
        """
        SELECT
            risk_level,
            COUNT(*) as total
        FROM AnalysisHistory
        GROUP BY risk_level
        """
    )

    return cursor.fetchall()
def confidence_trend():

    cursor.execute(
        """
        SELECT
            analysis_id,
            confidence_score
        FROM AnalysisHistory
        ORDER BY analysis_id ASC
        LIMIT 10
        """
    )

    return cursor.fetchall()