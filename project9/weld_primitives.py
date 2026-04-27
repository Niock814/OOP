import math
import logging
from abc import ABC, abstractmethod
from exceptions import InvalidParameterError

logger = logging.getLogger(__name__)

class WeldPrimitive(ABC):
    
    def __init__(self, length: float, material_density: float, strength_coeff: float):
        self._length = length
        self._material_density = material_density
        self._strength_coeff = strength_coeff
        self._validate()
        logger.info(f"Создан {self.__class__.__name__}: длина={length} мм")
    
    def _validate(self):
        if self._length <= 0:
            raise InvalidParameterError("Длина примитива должна быть положительной")
        if self._material_density <= 0:
            raise InvalidParameterError("Плотность материала должна быть положительной")
        if not (0 < self._strength_coeff <= 1):
            raise InvalidParameterError("Коэффициент прочности должен быть в (0,1]")
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if value <= 0:
            raise InvalidParameterError("Длина не может быть <= 0")
        old = self._length
        self._length = value
        logger.debug(f"{self.__class__.__name__}: длина изменена {old} -> {value}")
    
    @abstractmethod
    def get_volume(self) -> float:
        pass
    
    @abstractmethod
    def get_mass(self) -> float:
        pass
    
    @abstractmethod
    def get_strength(self) -> float:
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}: L={self._length} мм, p={self._material_density} г/см³"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self._length}, {self._material_density}, {self._strength_coeff})"
    
    def __eq__(self, other):
        if not isinstance(other, WeldPrimitive):
            return False
        return (self._length == other._length and 
                self._material_density == other._material_density and
                self._strength_coeff == other._strength_coeff)


class ButtWeld(WeldPrimitive):
    
    def __init__(self, length: float, material_density: float, strength_coeff: float, thickness: float = 5.0):
        super().__init__(length, material_density, strength_coeff)
        self._thickness = thickness
        if thickness <= 0:
            raise InvalidParameterError("Толщина стыка должна быть > 0")
    
    def get_volume(self) -> float:
        return self._length * self._thickness * 10.0
    
    def get_mass(self) -> float:
        volume_cm3 = self.get_volume() / 1000.0
        return volume_cm3 * self._material_density
    
    def get_strength(self) -> float:
        return self._length * self._strength_coeff * 0.9


class FilletWeld(WeldPrimitive):
    
    def __init__(self, length: float, material_density: float, strength_coeff: float, leg: float = 4.0):
        super().__init__(length, material_density, strength_coeff)
        self._leg = leg
        if leg <= 0:
            raise InvalidParameterError("Катет углового шва должен быть > 0")
    
    def get_volume(self) -> float:
        area = (self._leg ** 2) / 2.0
        return self._length * area
    
    def get_mass(self) -> float:
        volume_cm3 = self.get_volume() / 1000.0
        return volume_cm3 * self._material_density
    
    def get_strength(self) -> float:
        return self._length * self._strength_coeff * 0.7


class EdgeWeld(WeldPrimitive):
    
    def __init__(self, length: float, material_density: float, strength_coeff: float, flange_width: float = 8.0):
        super().__init__(length, material_density, strength_coeff)
        self._flange_width = flange_width
        if flange_width <= 0:
            raise InvalidParameterError("Ширина полки должна быть > 0")
    
    def get_volume(self) -> float:
        return self._length * (self._flange_width * 2 + 5.0)
    
    def get_mass(self) -> float:
        volume_cm3 = self.get_volume() / 1000.0
        return volume_cm3 * self._material_density
    
    def get_strength(self) -> float:
        return self._length * self._strength_coeff * 0.8