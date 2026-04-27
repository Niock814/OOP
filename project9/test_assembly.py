import pytest
from weld_primitives import ButtWeld
from assembly import Assembly, DrawingUpdater, MassReporter
from exceptions import IncompatiblePrimitiveError, AssemblyNotFoundError

def test_add_primitive():
    asm = Assembly("Test")
    b = ButtWeld(100, 7.85, 0.9)
    asm.add_primitive(b)
    assert len(asm.primitives) == 1

def test_add_invalid():
    asm = Assembly("Test")
    with pytest.raises(IncompatiblePrimitiveError):
        asm.add_primitive("not a primitive")

def test_remove_out_of_range():
    asm = Assembly("Test")
    with pytest.raises(AssemblyNotFoundError):
        asm.remove_primitive(10)

def test_observer_notification():
    asm = Assembly("Test")
    updater = DrawingUpdater()
    asm.attach(updater)
    b = ButtWeld(100, 7.85, 0.9)
    asm.add_primitive(b)
    assert len(asm.primitives) == 1