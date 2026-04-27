import pytest
from weld_primitives import ButtWeld, FilletWeld, EdgeWeld
from exceptions import InvalidParameterError

def test_butt_weld_creation():
    b = ButtWeld(100, 7.85, 0.9, thickness=5)
    assert b.length == 100
    assert b.get_mass() > 0

def test_invalid_length():
    with pytest.raises(InvalidParameterError):
        ButtWeld(-10, 7.85, 0.9)

def test_fillet_weld_strength():
    f = FilletWeld(50, 7.85, 0.8, leg=4)
    assert f.get_strength() == 50 * 0.8 * 0.7

def test_edge_weld_volume():
    e = EdgeWeld(100, 7.85, 0.9, flange_width=8)
    assert e.get_volume() == 100 * (8*2 + 5)