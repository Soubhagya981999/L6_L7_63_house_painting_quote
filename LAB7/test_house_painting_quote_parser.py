import pytest
from hypothesis import given, strategies as st

from house_painting_quote_parser import (
    clean_colour_name,
    room_area,
    total_wall_area
)


# Test 1: Colour name validation
@given(st.lists(
    st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1),
    min_size=1
))
def test_clean_colour_name(words):
    name = " ".join(words)
    expected = "_".join(words)
    assert clean_colour_name(name) == expected


@pytest.mark.parametrize("value", ["", "   ", None, 123])
def test_invalid_colour_name(value):
    with pytest.raises((ValueError, TypeError)):
        clean_colour_name(value)


# Test 2: Room area calculation
@given(
    st.integers(min_value=1, max_value=10000),
    st.integers(min_value=1, max_value=10000)
)
def test_room_area(length, width):
    text = f"{length}x{width}"
    assert room_area(text) == length * width


@pytest.mark.parametrize(
    "value",
    ["", "12", "12x", "x10", "12x10x5",
     "abcx10", "-5x10", "0x10"]
)
def test_invalid_room_area(value):
    with pytest.raises(ValueError):
        room_area(value)


# Test 3: Total wall area calculation
@given(
    st.lists(
        st.integers(min_value=1, max_value=10000),
        min_size=1,
        max_size=20
    )
)
def test_total_wall_area(areas):
    text = ";".join(map(str, areas))
    assert total_wall_area(text) == sum(areas)


@pytest.mark.parametrize(
    "value",
    ["", "100;", ";100", "100;;200",
     "abc;100", "-50;100", "0;100"]
)
def test_invalid_wall_area(value):
    with pytest.raises(ValueError):
        total_wall_area(value)