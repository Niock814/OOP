import datetime
import pandas as pd
import numpy as np
import os
from LoadCell import LoadCell
from Composit import Container

def generate_sensor_csv(filename="sensor_data_cleaned.csv"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)
    
    test_sensors = LoadCell.generate_test_data(20, c_range=(50, 500), s_range=(1.0, 3.0), v_range=(5, 24))
    for sensor in test_sensors:
        Container.add_device(sensor)

    records = []
    start_time = datetime.datetime(2025, 1, 1, 0, 0, 0)
    
    for sensor in Container.get_load_cells():
        for day in range(7):
            for hour in range(24):
                meas_time = start_time + datetime.timedelta(days=day, hours=hour)
                sensor.timestamp = meas_time
                
                load_ratio = (hour / 24) * 0.8 + 0.2
                current_load = sensor.carrying * load_ratio
                try:
                    sensor.add_load(current_load)
                except:
                    sensor.tare()
                    sensor.add_load(current_load * 0.9)
                
                temp = 20 + 5 * np.sin(2 * np.pi * (hour - 6) / 24) + 0.01 * current_load + np.random.normal(0, 1.5)
                
                pressure_base = 1013 + 10 * np.sin(2 * np.pi * (day*24 + hour) / (24*7))
                pressure_noise = np.random.normal(0, 1.5)
                pressure = pressure_base + pressure_noise
                
                if pressure < 1005:
                    vibration = 0.5 + np.random.exponential(0.15) + 0.4
                elif pressure < 1010:
                    vibration = 0.5 + np.random.exponential(0.15) + 0.2
                elif pressure > 1020:
                    vibration = 0.5 + np.random.exponential(0.15) + 0.3
                else:
                    vibration = 0.5 + np.random.exponential(0.12)
                
                records.append({
                    "timestamp": meas_time,
                    "temperature_c": round(temp, 2),
                    "pressure_hpa": round(pressure, 2),
                    "vibration_mm_s": round(vibration, 3)
                })
                
                sensor.tare()
    
    df = pd.DataFrame(records)
    df["pressure_bar"] = df["pressure_hpa"] / 1000
    df.drop("pressure_hpa", axis=1, inplace=True)
    
    df.to_csv(filepath, index=False)
    print(f"Создан файл: {filepath}, записей: {len(df)}")
    return df

if __name__ == "__main__":
    generate_sensor_csv()