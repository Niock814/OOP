from Class1 import ControlValve
from Base import equipment

data = ControlValve.generate_test_data(100, d_range=(10, 20), p_range=(1, 2))

equipment.save_to_csv("data.csv", data)
equipment.save_to_json("data.json", data)

for item in data[:5]:
        
     print(item.to_dict())