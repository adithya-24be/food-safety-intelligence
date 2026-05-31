from db import cursor

def get_restaurant_metrics(restaurant_name):

    cursor.execute(
        """
        SELECT
            rating,
            total_orders,
            complaints,
            refunds
        FROM Restaurant
        WHERE restaurant_name = %s
        """,
        (restaurant_name,)
    )

    return cursor.fetchone()