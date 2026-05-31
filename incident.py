from db import conn, cursor

def save_incidents(
    restaurant_name,
    detected
):

    for issue in detected:

        cursor.execute(
            """
            INSERT INTO RestaurantIncidents
            (
                restaurant_name,
                issue_type
            )
            VALUES (%s, %s)
            """,
            (
                restaurant_name,
                issue
            )
        )

    conn.commit()