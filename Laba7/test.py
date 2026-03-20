import pytest
import datetime
from Class1 import ControlValve
from Class2 import LoadCell
from Base import equipment

def test_prinadleghnost():

        load_cell = LoadCell("Test", 100, 2.0, 10, "C3")
        valve = ControlValve("Test", 50, 16, 0.5, "Электрический")
        
        assert isinstance(load_cell, equipment)
        assert isinstance(valve, equipment)
        assert issubclass(LoadCell, equipment)
        assert issubclass(ControlValve, equipment)

def test_atribyti():

        load_cell = LoadCell("LC123", 100, 2.0, 10, "C3")
        valve = ControlValve("CV456", 50, 16, 0.5, "Электрический")
        
        assert load_cell.model == "LC123"
        assert valve.model == "CV456"
        assert isinstance(load_cell.timestamp, datetime.datetime)
        assert isinstance(valve.timestamp, datetime.datetime)

def test_ravenstvo():
        load_cell2 = LoadCell("LC123", 100, 2.0, 10, "C3")
        load_cell1 = LoadCell("LC123", 100, 2.0, 10, "C3")

        assert load_cell2 == load_cell1