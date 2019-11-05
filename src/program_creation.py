import datetime
import warnings

import main


class CreateProgram(main.Main):
    def __init__(self):
        super().__init__()


class DecompressionProgram(CreateProgram):
    def __init__(self):
        super().__init__()


class QuasiContinuousProgram(DecompressionProgram):
    def __init__(self):
        super().__init__()


class LinearQuasiContinuousProgram(QuasiContinuousProgram):
    def __init__(self):
        self.starting_pressure: float = float()
        self.ending_pressure: float = float()
        self.duration: int = int()
        super().__init__()

    def get_program_parameters(self):
        # ToDo find the maximum change per second.

        def validate_duration(duration):

            if not isinstance(duration, int):
                raise ValueError(
                    "Error: duration expected as a non-negative, non-zero int."
                )

            if duration < 1:
                raise ValueError(
                    "Error: duration expected as a non-negative, non-zero int."
                )

            if duration > 604800:
                days = datetime.timedelta(seconds=duration).days

                warnings.warn(
                    "Warning: the duration specified is {} days. Is this correct?".format(
                        days
                    )
                )

        def validate_pressure(pressure):

            if not isinstance(pressure, float):
                raise ValueError(
                    "Error: pressure expected as a non-negative, non-zero float."
                )

            if pressure < 1.0:
                raise ValueError(
                    "Error: pressure expected as a non-negative, non-zero float."
                )

            if pressure > 250.0:
                warnings.warn("Warning: the pressure specified is above 250MPa.")

        def check_start_and_end_pressure(start, end):
            if start <= end:
                warnings.warn("Warning: The start pressure is lower than the end pressure.")

        print(
            "Please input the following parameters: Length of program (seconds), starting pressure (MPa) "
            "and ending pressure (MPa): \n \n"
        )
        program_duration = input("Please enter the length of the program in seconds:")
        program_duration = int(program_duration)
        try:
            validate_duration(duration=program_duration)
        except ValueError:
            # ToDo reset
            raise
        print("{} seconds".format(program_duration))

        starting_pressure = input("Please enter the starting pressure in MPa:")
        starting_pressure = float(starting_pressure)
        try:
            validate_pressure(pressure=starting_pressure)
        except ValueError:
            # ToDo reset
            raise
        print("Starting pressure: {}".format(starting_pressure))

        ending_pressure = input("Please enter the ending pressure in MPa:")
        ending_pressure = float(ending_pressure)
        try:
            validate_pressure(pressure=ending_pressure)
        except ValueError:
            # ToDo reset
            raise
        print("Ending pressure: {}".format(ending_pressure))

        check_start_and_end_pressure(start=starting_pressure, end=ending_pressure)

        self.duration = program_duration
        self.starting_pressure = starting_pressure
        self.ending_pressure = ending_pressure
