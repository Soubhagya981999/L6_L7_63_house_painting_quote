
import pytest
from house_painting_quote import painting_quote, paint_litres, crew_days


def test_unknown_paint():
    with pytest.raises(ValueError):
        painting_quote("oil", 500, 2, False)


def test_invalid_area():
    with pytest.raises(ValueError):
        painting_quote("emulsion", 0, 2, False)


def test_invalid_coats():
    with pytest.raises(ValueError):
        painting_quote("emulsion", 500, 0, False)


def test_distemper_exterior():
    with pytest.raises(ValueError):
        painting_quote("distemper", 500, 2, True)


def test_interior_emulsion():
    assert painting_quote("emulsion", 500, 2, False) == 20000


def test_exterior_enamel():
    assert painting_quote("enamel", 500, 2, True) == 32500


def test_large_area_discount():
    assert painting_quote("emulsion", 2500, 2, False) == 90000


def test_area_at_discount_boundary():
    assert painting_quote("emulsion", 2000, 2, False) == 80000


def test_minimum_cost():
    assert painting_quote("distemper", 100, 1, False) == 5000


def test_cost_above_minimum():
    assert painting_quote("enamel", 500, 1, False) == 15000


def test_smooth_surface():
    assert paint_litres(200, 1, "smooth") == 2


def test_rough_surface():
    assert paint_litres(120, 1, "rough") == 2


def test_unknown_surface():
    with pytest.raises(ValueError):
        paint_litres(100, 1, "wood")


def test_exact_litre_calculation():
    assert paint_litres(200, 1, "smooth") == 2


def test_remaining_litres():
    assert paint_litres(201, 1, "smooth") == 3


def test_invalid_painters():
    with pytest.raises(ValueError):
        crew_days(1000, 0, False)


def test_valid_painters():
    assert crew_days(800, 2, False) == 1


def test_remaining_work():
    assert crew_days(1000, 2, False) == 2


def test_wallpaper_removal():
    assert crew_days(800, 2, True) == 3


def test_no_wallpaper_removal():
    assert crew_days(800, 2, False) == 1
