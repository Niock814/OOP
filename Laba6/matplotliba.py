import random
from main import LoadCell
import matplotlib.pyplot as plt



sensors = LoadCell.generate_test_data(10, c_range=(10, 150), s_range=(0.2, 5), v_range=(2,36))

loads = []  
times = []  
voltage = []
max_output = []

for sensor in sensors:
        
        random_load = round(random.uniform(0, sensor.carrying * 0.7),1)
        sensor.add_load(random_load)

        loads.append(sensor.current_load)
        times.append(sensor.timestamp)
        

 
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Графики тензодатчиков', fontsize=14)
    
    
ax1.plot(times, loads, 'bo-', markersize=8, linewidth=2)
ax1.set_xlabel('Время')
ax1.set_ylabel('Нагрузка (Кг)')
ax1.set_title('Нагрузка на датчиках по времени')
ax1.grid(True, alpha=0.3)
    
    # Поворачиваем подписи времени для лучшей читаемости
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
    
    
    # График 2: Сравнение грузоподъемности и текущей нагрузки

voltage_values = []
max_output_values = []

# Создаем датчик с чувствительностью 0.5 мВ/В
tanzor = LoadCell("Консольный", 100, 0.5, 2, "C1")

# Изменяем напряжение от 2 до 36 В с шагом 2
for voltage_val in range(2, 38, 2):
    tanzor.voltage = voltage_val
    voltage_values.append(tanzor.voltage)
    max_output_values.append(tanzor.max_output())
    

# Строим график
ax2.plot(voltage_values, max_output_values, 'ro-', markersize=8, linewidth=2, label='Выходной сигнал')
ax2.set_xlabel('Напряжение питания (В)', fontsize=12)
ax2.set_ylabel('Максимальный выход (мВ)', fontsize=12)
ax2.set_title('Зависимость максимального выхода от напряжения', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend()



plt.tight_layout()
plt.savefig('Laba6\chartlaba6.png', dpi=150)
plt.show()
print(f"\nГрафик сохранен как 'simple_sensors_with_time.png'")