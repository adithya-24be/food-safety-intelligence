from db import cursor

def get_review_score(restaurant_name):

    cursor.execute(
        """
        SELECT sentiment
        FROM Reviews
        WHERE restaurant_name = %s
        """,
        (restaurant_name,)
    )

    reviews = cursor.fetchall()

    positive = 0
    negative = 0

    for review in reviews:

        if review[0] == "positive":
            positive += 1

        elif review[0] == "negative":
            negative += 1

    score = (positive * 5) - (negative * 5)

    return score