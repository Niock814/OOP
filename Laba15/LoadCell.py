import random
import datetime
from exception import InvalidParameterError, MeasurementError

class LoadCell:
    def __init__(self, model, carrying, sensitivity, voltage, accuracy_class):
        self.__model = model
        self.__carrying = carrying
        self.__sensitivity = sensitivity
        self.__voltage = voltage
        self.__accuracy_class = accuracy_class
        self.__current_load = 0.0
        self.__timestamp = datetime.datetime.now()
        self.__is_enabled = True

    @property
    def current_load(self):
        return self.__current_load

    @property
    def model(self):
        return self.__model

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if carrying > 0:
            self.__carrying = carrying
        else:
            raise InvalidParameterError("ERROR: Carrying capacity must be positive")

    @property
    def sensitivity(self):
        return self.__sensitivity

    @sensitivity.setter
    def sensitivity(self, sensitivity):
        if sensitivity > 0:
            self.__sensitivity = sensitivity
        else:
            raise InvalidParameterError("ERROR: Sensitivity must be positive")

    @property
    def voltage(self):
        return self.__voltage

    @voltage.setter
    def voltage(self, voltage):
        if voltage > 0:
            self.__voltage = voltage
        else:
            raise InvalidParameterError("ERROR: Voltage must be positive")

    @property
    def accuracy_class(self):
        return self.__accuracy_class

    @accuracy_class.setter
    def accuracy_class(self, accuracy_class):
        valid_classes = ["C1", "C2", "C3", "C4", "C5", "C6"]
        if accuracy_class in valid_classes:
            self.__accuracy_class = accuracy_class
        else:
            raise InvalidParameterError("ERROR: Accuracy class must be C1-C6")

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, value):
        if isinstance(value, datetime.datetime):
            self.__timestamp = value
        else:
            raise InvalidParameterError("ERROR: Timestamp must be datetime object")

    def enable(self):
        self.__is_enabled = True

    def disable(self):
        self.__is_enabled = False

    def measure(self):
        if not self.__is_enabled:
            raise MeasurementError("ERROR: Sensor is disabled, measurement impossible")
        return self.__current_load

    def __str__(self):
        return(f"Модель: {self.__model}\nГрузоподъемность: {self.__carrying} кг\nЧувствительность: {self.__sensitivity} мВ/В\nНапряжение: {self.__voltage} В\nКласс точности: {self.__accuracy_class}\nТочность: {self.accuracy()}\nМаксимальный выход: {self.max_output()} мВ\nТекущая нагрузка: {self.__current_load} кг")

    def __repr__(self):
        return (f"LoadCell(model={self.__model!r}, carrying={self.__carrying}, sensitivity={self.__sensitivity}, voltage={self.__voltage}, accuracy_class={self.__accuracy_class!r})")

    def to_dict(self):
        return {
            "model": self.__model,
            "carrying": self.__carrying,
            "sensitivity": self.__sensitivity,
            "voltage": self.__voltage,
            "accuracy_class": self.__accuracy_class,
            "current_load": self.__current_load,
            "time": self.__timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }

    def __eq__(self, other):
        if not isinstance(other, LoadCell):
            return NotImplemented
        return self.model == other.model

    def __add__(self, other):
        if not isinstance(other, LoadCell):
            return NotImplemented
        return LoadCell(
            self.model,
            self.carrying + other.carrying,
            self.sensitivity + other.sensitivity,
            self.voltage + other.voltage,
            self.accuracy_class
        )

    def max_output(self):
        return round(self.__sensitivity * self.__voltage, 2)

    def accuracy(self):
        acc_map = {"C1": 0.05, "C2": 0.03, "C3": 0.02, "C4": 0.015, "C5": 0.012, "C6": 0.008}
        if self.__accuracy_class in acc_map:
            return acc_map[self.__accuracy_class]
        else:
            raise InvalidParameterError("ERROR: Unknown accuracy class")

    def add_load(self, load):
        if load < 0:
            raise InvalidParameterError("ERROR: Load cannot be negative")
        new_load = self.__current_load + load
        if new_load > self.__carrying:
            raise InvalidParameterError("ERROR: Load exceeds carrying capacity")
        else:
            self.__current_load = new_load

    def weight(self):
        if not self.__is_enabled:
            raise MeasurementError("ERROR: Sensor is disabled")
        return self.__current_load

    def tare(self):
        self.__current_load = 0.0

    @staticmethod
    def generate_test_data(n, **kwargs):
        data_list = []
        accuracys = ["C1", "C2", "C3", "C4", "C5", "C6"]
        c_min, c_max = kwargs.get('c_range', (10, 400))
        s_min, s_max = kwargs.get('s_range', (0.1, 10))
        v_min, v_max = kwargs.get('v_range', (5, 24))
        start_time = datetime.datetime.now()
        delta = datetime.timedelta(seconds=10)

        for i in range(n):
            carrying = random.randint(c_min, c_max)
            sensivity = round(random.uniform(s_min, s_max), 1)
            voltage = random.randint(v_min, v_max)
            model = "LC" + str(random.randint(100, 999))
            accuracy_class = random.choice(accuracys)
            obj = LoadCell(model, carrying, sensivity, voltage, accuracy_class)
            obj.timestamp = start_time + (delta * i)
            data_list.append(obj)

        return data_list