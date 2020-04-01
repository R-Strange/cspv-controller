import datetime
from collections import namedtuple
from dataclasses import dataclass, fields
from typing import List, Tuple, Mapping
import pandas as pd
from string import Template


@dataclass
class DecompressionProgram:
    creation_date: datetime.datetime
    payload: pd.DataFrame
    duration: int
    type_of_program: str
    user_verification: bool = False
    is_complete: bool = False
    is_correct: bool = False

    def datatype_check(self) -> Tuple:

        datatype_checks: List[object] = [
            isinstance(self.creation_date, datetime.datetime),
            isinstance(self.payload, pd.DataFrame),
            isinstance(self.duration, int),
            isinstance(self.user_verification, bool),
            isinstance(self.type_of_program, str),
        ]

        passed: bool = all(datatype_checks)

        status_message: str = "datatype check failed"

        if passed:
            status_message: str = "datatype check passed"

        return passed, status_message

    def completion_check(self) -> bool:
        """ returns a bool of if all data needed to execute a program is present

        :return: is_complete: bool, all information is present to run the program.
        """

        is_creation_date_complete = self.creation_date is not None
        is_payload_complete = not self.payload.empty
        is_duration_complete = self.duration is not None
        is_user_verification_complete = self.user_verification is True

        completeness_checks = [
            is_creation_date_complete,
            is_duration_complete,
            is_payload_complete,
            is_user_verification_complete,
        ]

        return all(completeness_checks)

    def is_feasible(self):

        pass

    def _default_dict_type(self):
        """Literal for """
