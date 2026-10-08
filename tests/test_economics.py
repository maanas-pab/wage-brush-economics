from src.economics import brush_label, hours_to_earn, paint_multiplier, wage_to_brush


def test_endpoints():
    assert wage_to_brush(7) == 1
    assert wage_to_brush(500) == 60


def test_monotonic():
    assert wage_to_brush(7.25) < wage_to_brush(29) < wage_to_brush(500)


def test_labels():
    assert "Hairline" in brush_label(1)
    assert "Roller" in brush_label(35) or "sprayer" in brush_label(60).lower()


def test_labor_math():
    assert paint_multiplier(500) > 10
    assert hours_to_earn(2000, 7.25) > hours_to_earn(2000, 500)
