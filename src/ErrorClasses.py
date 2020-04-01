from serial.serialutil import SerialException, SerialTimeoutException


class BaseSerialConnectionErrorClass(SerialException):
    pass


class BaseSerialTimeoutErrorClass(SerialTimeoutException):
    pass


class NoPortsDetectedError(BaseSerialConnectionErrorClass):
    pass


class NoArduinoDevicesDetectedError(BaseSerialConnectionErrorClass):
    pass

class MultipleArduinoDevicesConnectedError(BaseSerialConnectionErrorClass):
    pass
