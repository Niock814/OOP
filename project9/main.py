import os
from logger_setup import setup_logging
from weld_primitives import ButtWeld, FilletWeld, EdgeWeld
from assembly import Assembly, DrawingUpdater, MassReporter, StrengthChecker
from data_generator import generate_assemblies, save_to_csv, save_to_json
from visualization import plot_mass_distribution, plot_strength_vs_length
import logging

os.makedirs("project9", exist_ok=True)
setup_logging()
logger = logging.getLogger(__name__)

assembly = Assembly("MainFrame")
drawing = DrawingUpdater()
mass_reporter = MassReporter()
strength_checker = StrengthChecker()

assembly.attach(drawing)
assembly.attach(mass_reporter)
assembly.attach(strength_checker)

try:
    butt = ButtWeld(120, 7.85, 0.95, thickness=6)
    fillet = FilletWeld(80, 7.85, 0.85, leg=5)
    edge = EdgeWeld(150, 7.85, 0.90, flange_width=10)
    
    assembly.add_primitive(butt)
    assembly.add_primitive(fillet)
    assembly.add_primitive(edge)
    
    assembly.remove_primitive(1)
except Exception as e:
    logger.error(f"Ошибка: {e}")

print(f"\nСборка: {assembly.name}")
print(f"Примитивов: {len(assembly.primitives)}")
print(f"Общая масса: {assembly.calculate_total_mass():.2f} г")
print(f"Прочности: {[round(s,2) for s in assembly.get_strength_report()]}")

assemblies = generate_assemblies(10, 10)
save_to_csv(assemblies)
save_to_json(assemblies)

plot_mass_distribution(assemblies)
plot_strength_vs_length(assemblies)

print(f"\nВсе файлы сохранены в папку: project9/")
print(f"Сгенерировано сборок: {len(assemblies)}")
print(f"Всего примитивов: {sum(len(a.primitives) for a in assemblies)}")

logger.info("Демонстрация завершена")