from LoadCell import LoadCell
from generation import generate_test_data
from save import save_to_csv, save_to_json



data = generate_test_data(50, c_range=(10, 150), s_range=(0.2, 5), v_range=(2,36))

save_to_json("datata.json", data)
save_to_csv("datata.csv", data)

tanzor = LoadCell("Консольный", 100, 0.5, 12,"C1")
tanzor.add_load(20)
tanzor.add_load(40)
