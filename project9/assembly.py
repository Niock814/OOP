import logging
from typing import List, Dict, Any
from weld_primitives import WeldPrimitive
from exceptions import IncompatiblePrimitiveError, AssemblyNotFoundError

logger = logging.getLogger(__name__)

class Observer:
    def update(self, subject: 'Assembly', event_type: str, data: Dict[str, Any]):
        pass

class DrawingUpdater(Observer):
    def update(self, subject, event_type, data):
        logger.info(f"[DrawingUpdater] Чертеж обновлен: событие {event_type}, примитивов теперь {len(subject.primitives)}")

class MassReporter(Observer):
    def update(self, subject, event_type, data):
        total_mass = subject.calculate_total_mass()
        logger.info(f"[MassReporter] Текущая масса сборки: {total_mass:.2f} г")

class StrengthChecker(Observer):
    def update(self, subject, event_type, data):
        if subject.primitives:
            strengths = [p.get_strength() for p in subject.primitives]
            min_strength = min(strengths)
            logger.info(f"[StrengthChecker] Минимальная прочность: {min_strength:.2f}")

class Assembly:
    
    def __init__(self, name: str):
        self._name = name
        self._primitives: List[WeldPrimitive] = []
        self._observers: List[Observer] = []
        logger.info(f"Создана сборка '{name}'")
    
    @property
    def name(self):
        return self._name
    
    @property
    def primitives(self):
        return self._primitives.copy()
    
    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
            logger.debug(f"Наблюдатель {observer.__class__.__name__} подписан на сборку {self._name}")
    
    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
            logger.debug(f"Наблюдатель {observer.__class__.__name__} отписан")
    
    def _notify(self, event_type: str, data: Dict[str, Any] = None):
        for obs in self._observers:
            try:
                obs.update(self, event_type, data or {})
            except Exception as e:
                logger.error(f"Ошибка в наблюдателе {obs.__class__.__name__}: {e}")
    
    def add_primitive(self, primitive: WeldPrimitive):
        if not isinstance(primitive, WeldPrimitive):
            raise IncompatiblePrimitiveError("Можно добавлять только объекты WeldPrimitive")
        self._primitives.append(primitive)
        logger.info(f"В сборку '{self._name}' добавлен {primitive.__class__.__name__}")
        self._notify("add", {"primitive": primitive})
    
    def remove_primitive(self, index: int):
        if index < 0 or index >= len(self._primitives):
            raise AssemblyNotFoundError(f"Примитив с индексом {index} не найден")
        removed = self._primitives.pop(index)
        logger.info(f"Из сборки '{self._name}' удалён {removed.__class__.__name__}")
        self._notify("remove", {"primitive": removed})
    
    def calculate_total_mass(self) -> float:
        total = sum(p.get_mass() for p in self._primitives)
        logger.debug(f"Пересчитана общая масса сборки '{self._name}': {total:.2f} г")
        return total
    
    def calculate_total_volume(self) -> float:
        return sum(p.get_volume() for p in self._primitives)
    
    def get_strength_report(self) -> List[float]:
        return [p.get_strength() for p in self._primitives]
    
    def __str__(self):
        return f"Сборка '{self._name}': {len(self._primitives)} примитивов, масса={self.calculate_total_mass():.2f} г"
    
    def __repr__(self):
        return f"Assembly('{self._name}', primitives={self._primitives})"
    
    def __eq__(self, other):
        if not isinstance(other, Assembly):
            return False
        return self._name == other._name