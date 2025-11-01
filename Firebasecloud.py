from datetime import datetime

def get_season(month):
    """Return the season based on month."""
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "summer"
    elif month in [6, 7, 8, 9]:
        return "monsoon"
    else:
        return "autumn"

def dynamic_pricing(base_price, car_type, region):
    """Calculate adjusted price based on region and season."""
    month = datetime.now().month
    season = get_season(month)

    region_multipliers = {
        "hilly": 1.10 if car_type in ["SUV", "off-road"] else 0.95,
        "metro": 0.97 if car_type in ["hatchback", "sedan"] else 1.03,
        "rural": 1.05 if car_type in ["pickup", "SUV"] else 0.98
    }

    season_multipliers = {
        "monsoon": 1.08 if car_type in ["SUV", "off-road"] else 0.94,
        "summer": 1.03,
        "winter": 1.00,
        "autumn": 0.99
    }

    # Default multipliers if region not recognized
    region_factor = region_multipliers.get(region, 1.0)
    season_factor = season_multipliers.get(season, 1.0)

    adjusted_price = base_price * region_factor * season_factor

    return {
        "base_price": base_price,
        "region": region,
        "season": season,
        "car_type": car_type,
        "recommended_price": round(adjusted_price, 2)
    }

# Example Usage
example_1 = dynamic_pricing(1000000, "SUV", "hilly")
example_2 = dynamic_pricing(700000, "hatchback", "metro")

print("Example 1:", example_1)
print("Example 2:", example_2)
