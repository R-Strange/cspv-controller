import serial
import pyfirmata
import time
from serial.tools import list_ports
from typing import List
from src.ErrorClasses import *


def detect_ports() -> List[str]:

    list_of_ports: list = list_ports

    for port in list_ports.comports():
        list_of_ports.append(port)

    return list_of_ports


def find_arduino_ports(verbose: bool = False) -> List[str]:

    ports: list = list_ports.comports()

    if verbose:

        if len(ports) == 0:
            print("No ports found")
            raise NoPortsDetectedError("Error: No USB connections detected. Is your Arduino connected?")

        else:
            devices = [port.device for port in ports]
            descriptions = [port.description for port in ports]
            print("Ports detected: {}".format(devices))
            print("Details:")
            for description in descriptions:
                print(description)

    return [port.device for port in ports if "Arduino Uno" in port.description]


class ArduinoUno:

    def __init__(self, verbose=False):
        self.active: bool = False
        self.verbose: bool = verbose

        self.port: str = self.select_arduino_uno_port()
        self.connection = self.connect_to_arduino()

    def select_arduino_uno_port(self):

        ports = find_arduino_ports(verbose=self.verbose)

        if len(ports) == 0:
            raise NoPortsDetectedError("Error: No USB connection detected. Is your Arduino connected?")

        if len(ports) < 1:
            raise MultipleArduinoDevicesConnectedError("Error: Multiple Arduino Uno devices detected")

        port_device = ports[0]

        if self.verbose:
            print("Arduino Uno device detected and selected at serial {}".format(port_device))

        return port_device

    def connect_to_arduino(self) -> object:

        if self.verbose:
            print("connecting to Arduino serial port")
        connection: object = pyfirmata.Arduino(self.port)

        if self.verbose:
            print("waiting for Firmata initialisation to avoid port buffering errors")

        time.sleep(10)

        if self.verbose:
            print("Firmata initialised. Arduino Uno Connected")

        return connection
