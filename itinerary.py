def generate_itinerary(destination, days, budget, interests):
    daily_budget = budget // days
    interests = interests.lower()

    if "food" in interests:
        afternoon = "Try famous local food spots"
    elif "culture" in interests:
        afternoon = "Visit museums / heritage sites"
    else:
        afternoon = "Explore local area"

    itinerary = []

    for day in range(1, days + 1):
        itinerary.append({
            "day": day,
            "schedule": {
                "morning": f"Explore a famous place in {destination}",
                "afternoon": f"{afternoon} within ₹{daily_budget//3}",
                "evening": "Free attraction / market walk"
            },
            "estimated_cost": daily_budget
        })

    return itinerary
