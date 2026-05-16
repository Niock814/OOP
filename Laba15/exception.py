class DeviceError(Exception):
    pass

class InvalidParameterError(DeviceError):
    pass

class DeviceNotFoundError(DeviceError):
    pass

class MeasurementError(DeviceError):
    pass

class ObserverError(DeviceError):
    pass