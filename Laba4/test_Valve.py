import pytest
import math
from ControlValve import ControlValve


def test_init_and_getters():
    Valve = ControlValve("Мембранный", 40, 50, 0.75, "Гидравлический")
    assert Valve.model == "Мембранный"
    assert Valve.diameter == 40
    assert Valve.pressure == 50
    assert Valve.Kv == 0.75
    assert Valve.actuator_type == "Гидравлический"


def test_validation():
    Valve = ControlValve("Мембранный", 40, 50, 0.75, "Гидравлический")
    Valve.pressure = -60
    Valve.Kv = 0.95
    assert Valve.pressure == 50
    assert Valve.Kv == 0.95

def test_calculate():
    Valve = ControlValve("Мембранный", 40, 50, 0.75, "Гидравлический")
    assert Valve.flow_coefficient == Valve.Kv*math.sqrt(2)

def test_eq():
    valve1 = ControlValve("Седельный", 50, 10, 0.91, "Ручной")
    valve2 = ControlValve("Седельный", 30, 5, 0.75, "Гидравлический")
    valve3 = ControlValve("Клетчатый", 10, 100, 0.89, "Электрический")
    assert valve1 == valve2
    assert valve1 != valve3

def test_lt():
    valve1 = ControlValve("Седельный", 50, 10, 0.91, "Ручной")
    valve2 = ControlValve("Мембранный", 30, 5, 0.75, "Гидравлический")
    valve3 = ControlValve("Клетчатый", 10, 100, 0.89, "Электрический")
    assert valve1 > valve2
    assert not valve2 < valve3

def test_add():
    valve1 = ControlValve("Седельный", 50, 10, 0.90, "Гидравлический")
    valve2 = ControlValve("Седельный", 30, 5, 0.80, "Гидравлический")

    valve = valve1+valve2
    assert valve.diameter == 80
    assert valve.pressure == 15
    assert pytest.approx(valve.Kv) == pytest.approx(0.85)