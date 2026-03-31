from LoadCell import LoadCell
from ControlValve import ControlValve
from Base import equipment
import random


tanzor = LoadCell("Консольный", 100, 0.5, 12,"C1")
tanzor.add_load(75)
print(tanzor)

valve3 = ControlValve("Клетчатый", 10, 100, 0.89, "Электрический")
print(valve3)

def print_all(devices):
    for equipment in devices:
        print(f"\n{equipment.description()}")
        print(f"  Показание: {equipment.read_value()} {equipment.unit}")

load_cells = []
load_cells = LoadCell.generate_test_data(3, c_range=(50, 200), s_range=(1, 3), v_range=(10, 20))
for i in load_cells:
    i.add_load(random.uniform(10, i.carrying * 0.5))

valves = []
valves = ControlValve.generate_test_data(3, d_range=(20, 50), p_range=(10, 30))

all_devices=[]
all_devices = load_cells + valves

print_all(all_devices)