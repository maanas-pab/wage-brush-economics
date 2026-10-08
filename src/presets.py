"""Occupation presets anchored to 2024 US wage bands (BLS OES, rounded)."""

PRESETS = [
    {"job": "Federal minimum wage", "wage": 7.25, "note": "Hairline"},
    {"job": "Barista", "wage": 16.0, "note": "Service median"},
    {"job": "Warehouse associate", "wage": 19.5, "note": "Logistics"},
    {"job": "US median (all workers)", "wage": 29.0, "note": "BLS median ~$28-30"},
    {"job": "Registered nurse", "wage": 45.0, "note": "Skilled care"},
    {"job": "Software engineer", "wage": 75.0, "note": "Tech"},
    {"job": "Surgeon", "wage": 150.0, "note": "Top 1% professions"},
    {"job": "Fortune-500 CEO (hourly equiv)", "wage": 500.0, "note": "Giant roller"},
]


def preset_wages():
    return {p["job"]: p["wage"] for p in PRESETS}
