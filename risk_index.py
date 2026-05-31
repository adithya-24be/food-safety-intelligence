from db import cursor

def get_risk_penalty(restaurant_name):

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM RestaurantIncidents
        WHERE restaurant_name = %s
        """,
        (restaurant_name,)
    )

    total_incidents = cursor.fetchone()[0]

    if total_incidents < 5:
        return 0

    elif total_incidents < 10:
        return 5

    elif total_incidents < 20:
        return 10

    elif total_incidents < 50:
        return 15

    else:
        return 20