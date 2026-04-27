class CADError(Exception):
    pass

class InvalidParameterError(CADError):
    pass

class IncompatiblePrimitiveError(CADError):
    pass

class AssemblyNotFoundError(CADError):
    pass