"""Core economics: wage -> brush mapping + labor-value helpers."""

MIN_WAGE = 7
MAX_WAGE = 500
MIN_BRUSH = 1
MAX_BRUSH = 60


def wage_to_brush(wage: float, scale: str = "linear") -> int:
    """Map hourly wage ($7-$500) to brush width (1-60px).

    linear: honest 1:1 proportion.
    sqrt: softens the CEO roller so houses stay drawable (area-perception).
    """
    wage = max(MIN_WAGE, min(MAX_WAGE, wage))
    t = (wage - MIN_WAGE) / (MAX_WAGE - MIN_WAGE)
    if scale == "sqrt":
        t = t**0.5
    return int(round(MIN_BRUSH + t * (MAX_BRUSH - MIN_BRUSH)))


def brush_label(px: int) -> str:
    if px <= 4:
        return "Hairline 🪡"
    if px <= 10:
        return "Pencil ✏️"
    if px <= 22:
        return "House brush 🖌️"
    if px <= 40:
        return "Roller 🧱"
    return "Industrial sprayer 🚜"


def paint_multiplier(wage: float, base_wage: float = 7.25) -> float:
    """How many x more paint per stroke vs a minimum-wage worker."""
    return wage_to_brush(wage) / wage_to_brush(base_wage)


def hours_to_earn(price: float, wage: float) -> float:
    """Hours of work needed to afford `price` at `wage`."""
    return price / max(wage, 0.01)
