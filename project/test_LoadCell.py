import pytest

from LoadCell import LoadCell

def test_add_load():
    tanzor = LoadCell("Консольный", 100, 0.5, 12,"C1")
    tanzor.add_load(20)
    tanzor.add_load(40)

    assert round(tanzor.weight(),1) == 60

def test_add():
    tanzor1 = LoadCell("Консольный", 100, 0.5, 12,"C1")
    tanzor2 = LoadCell("Консольный", 100, 0.5, 12,"C1")

    tanzor = tanzor1+tanzor2

    assert tanzor.carrying == 200
    assert tanzor.sensitivity == 1
    assert tanzor.voltage == 24


def test_tare():
    tanzor = LoadCell("Консольный", 100, 0.5, 12,"C1")
    tanzor.add_load(30)
    tanzor.tare()

    assert tanzor.current_load == 0
