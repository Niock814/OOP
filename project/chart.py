from LoadCell import LoadCell
import matplotlib.pyplot as plt
from generation import generate_test_data
import random


sensors = generate_test_data(10, c_range=(10, 150), s_range=(0.2, 5), v_range=(2,36))

loads = []  
carrying = []  
times = []  

for sensor in sensors:
        
        random_load = round(random.uniform(0, sensor.carrying * 0.7),1)
        sensor.add_load(random_load)

        loads.append(sensor.current_load)
        carrying.append(sensor.carrying)
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
    
    # Добавляем значения над точками
for i, (time, load) in enumerate(zip(times, loads)):
        ax1.text(time, load + 2, f'{load:.1f}', ha='center', fontsize=9)
    
    # График 2: Сравнение грузоподъемности и текущей нагрузки
x = range(len(sensors))
    
bars1 = ax2.bar([i-0.2 for i in x], carrying, width=0.4, 
                     label='Грузоподъемность', color='skyblue', edgecolor='blue')
bars2 = ax2.bar([i+0.2 for i in x], loads, width=0.4, 
                     label='Текущая нагрузка', color='lightcoral', edgecolor='red')
    
ax2.set_xlabel('Номер датчика')
ax2.set_ylabel('Кг')
ax2.set_title('Сравнение грузоподъемности и текущей нагрузки')
ax2.set_xticks(x)
ax2.set_xticklabels([f'{i+1}' for i in x])
ax2.legend()
ax2.grid(True, axis='y', alpha=0.3)
    
   

    
plt.tight_layout()
plt.savefig('simple_sensors_with_time.png', dpi=150)
plt.show()
print(f"\nГрафик сохранен как 'simple_sensors_with_time.png'")