from analytics import (
    most_common_issue,
    worst_restaurant,
    total_incidents,
    incidents_by_restaurant,
    recent_analyses,
    average_confidence,
    risk_distribution,
    confidence_trend
)

def get_dashboard():

    return {
    "issue": most_common_issue(),
    "restaurant": worst_restaurant(),
    "total_incidents": total_incidents(),
    "restaurant_chart": incidents_by_restaurant(),
    "recent": recent_analyses(),
    "avg_confidence": float(average_confidence()),
    "risk_distribution": risk_distribution(),
    "confidence_trend": confidence_trend()
}