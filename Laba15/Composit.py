from LoadCell import LoadCell
from exception import InvalidParameterError, DeviceNotFoundError

class Container:
    all_devices = []
    _load_cells = []

    @classmethod
    def add_device(cls, device):
        if isinstance(device, LoadCell):
            cls._load_cells.append(device)
            cls.all_devices.append(device)
            print(f"Добавлен тензодатчик: {device.model}")
        else:
            raise InvalidParameterError("ERROR: Only LoadCell objects can be added")  

    @classmethod
    def delete_by_model(cls, model):
        for device in cls.all_devices:
            if device.model == model:
                cls.all_devices.remove(device)
                if device in cls._load_cells:
                    cls._load_cells.remove(device)
                print(f"Удален тензодатчик: {model}")
                return
        raise InvalidParameterError(f"ERROR: Device with model {model} not found") 

    @classmethod
    def _remove_from_all(cls, model):
        for i, device in enumerate(cls.all_devices):
            if device.model == model:
                cls.all_devices.pop(i)
                break

    @classmethod
    def get_all_devices(cls):
        return cls.all_devices.copy()

    @classmethod
    def get_load_cells(cls):
        return cls._load_cells.copy()

    @classmethod
    def print_all_devices(cls):
        if not cls.all_devices:
            print("Нет устройств в контейнере")
            return
        
        for device in cls.all_devices:
            print(f"\n{device}")

    @classmethod
    def get_total_capacity(cls):
        total = sum(device.carrying for device in cls._load_cells)
        return total

    @classmethod
    def clear_all(cls):
        cls._load_cells.clear()
        cls.all_devices.clear()
        print("Все устройства удалены")