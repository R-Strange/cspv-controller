import datetime
from collections import namedtuple
from dataclasses import dataclass, field
from typing import Mapping
import pandas as pd


@dataclass
class DecompressionProgram:

    # ToDo rename module

    creation_date: datetime.datetime = field(
        metadata={
            "unit": "datetime",
            "description": "datetimestamp of program creation",
        }
    )
    payload: pd.DataFrame = field(
        metadata={
            "unit": "pressure|seconds",
            "description": "the decompression program. two column dataframe containing the pressure at a given number "
                           "of seconds",
        }
    )
    duration: int = field()
    type_of_program: str
    user_verification: bool = False

    def dtypes_check(self) -> namedtuple:

        mapping_dict: Mapping = {
            "creation_date": isinstance(self.creation_date, datetime.datetime),
            "payload": isinstance(self.payload, pd.DataFrame),
            "duration": isinstance(self.duration, int),
            "user_verification": isinstance(self.user_verification, bool),
            "type_of_program": isinstance(self.type_of_program, str),
        }

        results: list = list()

        for class_attribute in vars(self):
            try:
                results.append(mapping_dict[class_attribute])
            except KeyError:
                continue

        is_correct = all(results)

        if is_correct:
            output_message = "All class attributes are correctly typed"
        else:
            output_message = "Warning: class attributes are incorrectly typed"

        dtypes_check_results = namedtuple("dtypes_check", "is_correct, output_message")
        return dtypes_check_results(is_correct, output_message)

    def is_complete(self) -> namedtuple:
        """ returns a bool of if all data needed to execute a program is present

        :return: is_complete: bool, all information is present to run the program.
        """

        mapping_dict: Mapping = {
            "creation_date": lambda x: x is None,
            "payload": lambda x: x.empty,
            "duration": lambda x: x is None,
            "user_verification": lambda x: x is False,
            "type_of_program": lambda x: x == "",
        }

        results: list = list()

        for class_attribute in vars(self):
            try:
                results.append(mapping_dict[class_attribute])
            except KeyError:
                continue

        is_complete = not any(results)

        if is_complete:
            output_message = "All class attributes are not empty"
        else:
            output_message = "Warning: class attributes are empty"

        data_check_results = namedtuple("data_check", "is_correct, output_message")
        return data_check_results(is_complete, output_message)

    def _default_dict_type(self):
        """Literal for """
        pass
