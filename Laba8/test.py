import pytest
from Base import equipment
from ControlValve import ControlValve
from LoadCell import LoadCell


def test_abstract_class_cannot_be_instantiated():

    with pytest.raises(TypeError):
        device = equipment("Test")

def test_loadcell_read_value():

    lc = LoadCell("Test", 100, 2.0, 10, "C3")
    assert lc.read_value() == 0.0
    
    lc.add_load(25.5)
    assert lc.read_value() == 25.5
    assert lc.unit == "кг"



def test_controlvalve_read_value():

    valve = ControlValve("Test", 50, 16, 0.5, "Электрический")
    assert valve.read_value() == 16
    
    assert valve.unit == "бар"   

def test_polymorphic_function():
    
    devices = [
        LoadCell("LC1", 100, 2.0, 10, "C3"),
        ControlValve("V1", 50, 16, 0.5, "Электрический")
    ]
    
    for i in devices:
        assert hasattr(equipment, 'read_value')
        assert hasattr(equipment, 'unit')
        assert callable(equipment.read_value)