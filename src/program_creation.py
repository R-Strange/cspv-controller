import datetime
import warnings
import numpy as np
import pandas as pd

import main


def search_for_dangerous_pressures(dataframe: pd.DataFrame) -> bool:
    bad_data: pd.DataFrame = dataframe.loc[dataframe["target pressure"] > 251]

    if bad_data.empty:
        return False

    else:
        print("Pressures exceeding safe limits in program:")
        print(bad_data)

        raise ValueError("Pressures exceeding safe limits in program.")


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
        super().__init__()
        self.starting_pressure: float = float()
        self.ending_pressure: float = float()
        self.duration: int = int()
        self.within_pressure_range: bool = bool()

    def get_program_parameters(self):
        # ToDo find the maximum change per second.
        # ToDo change errors to custom errors

        def validate_duration(duration):

            if not isinstance(duration, int):
                raise ValueError(
                    "Error: duration expected as a non-negative, non-zero int."
                )

            if duration <= 1:
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
                warnings.warn(
                    "Warning: The start pressure is lower than the end pressure."
                )

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

        self.duration, self.starting_pressure, self.ending_pressure = (
            program_duration,
            starting_pressure,
            ending_pressure,
        )

    def calculate_program_waypoints(self):

        pressure_target = np.flip(
            np.linspace(
                start=self.starting_pressure,
                stop=self.ending_pressure,
                num=self.duration,
            )
        )
        time_series = np.arange(start=0, stop=self.duration)

        program_df = pd.DataFrame(data=[pressure_target, time_series]).T
        program_df.columns = ["target pressure", "elapsed time (seconds)"]

        self.within_pressure_range = not search_for_dangerous_pressures(program_df)

        return program_df
