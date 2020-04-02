from dataclasses import dataclass
from typing import NamedTuple

from program_creation import LinearQuasiContinuousProgram
from arduino_controller import ArduinoUno
from ErrorClasses import *


def main(verbose=False):
    """
    Overarching Narrative:
    1. start program on laptop
    2. connect to arduino and pressure sensor
    3. create a decompression program
    4. run the program
    5. end the program and quench

    Activities this sprint

    1. start program on laptop
        * Confirmation of start-up

    2. connect to Arduino and pressure sensor
        * Test for connected Arduino Uno [Done]
        * Test for a connected pressure sensor
        * Connect to Arduino Uno [Done]
        * Connect to pressure sensor

    3. Create decompression program
        * Get program details from user as direct input [Done]
        * Create a quasi-continuous linear decompression program [Done]
        * Display a plot of the decompression program [Done]
        * Range limit checks within the program [Done]
        * User verification prior to run [Done]

    4. Run the program
        * Change the pressure
        * Self-calibration
        * Report errors
        * Range limit checks during the run
        * Unplanned termination

    5. End the program and quench
    """

    # run the initialisation module
    #    INPUTS: NONE
    #    PROCESSES: import all modules, verify installation
    #    OUTPUTS: diagnostic check bool
    #
    # run the connection module
    #    INPUTS: user inputs to verify the arduino and pressure sensors are connected
    #    PROCESSES: test to find the arduino and pressure sensors and establish connections with both
    #    OUTPUTS: connection objects for the arduino and pressure sensor
    #
    # run the program creation module
    #    INPUTS: user inputs (duration, start, end) and verification for the user
    #    PROCESSES: request the inputs, create the decompression program, check for limits, produce a plot and
    #       display it
    #    OUTPUTS: decompression program
    #
    # run the execution module
    #    INPUTS: decompression program, connectors, user input to start AND PAUSE
    #    PROCESSES: initialise the machine to starting conditions, step through the program, check limits,
    #       terminate quickly and report errors
    #    OUTPUTS: Success code
    #
    # run the termination module
    #    INPUTS: Success code
    #    PROCESSES: Terminate the program
    #    OUTPUTS: Termination code
    #

    initialisation_check: bool = bool()
    arduino_connector: object = None
    pressure_sensor_connector: object = None
    decompression_program: dataclass = None

    program_creator = LinearQuasiContinuousProgram()
    program_creator.get_program_parameters()
    program = program_creator.calculate_program_waypoints()


if __name__ == "__main__":
    print("main logic")

