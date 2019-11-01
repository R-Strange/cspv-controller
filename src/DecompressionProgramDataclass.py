import datetime
from collections import namedtuple
from dataclasses import dataclass, fields
from typing import List, NamedTuple, Mapping
import pandas as pd


@dataclass
class DecompressionProgram:
    creation_date: datetime.datetime
    payload: pd.DataFrame
    duration: int
    user_verification: bool
    type_of_program: str

    def data_check(self) -> namedtuple:
        data_check_results = namedtuple("Data_Check", "is_correct, output_message")

        mapping_dict: Mapping = {"creation_date": isinstance(self.creation_date, datetime.datetime),
                                 "payload": isinstance(self.payload, pd.DataFrame),
                                 "duration": isinstance(self.user_verification, bool),
                                 "type_of_program":
                                 }



        return results

    def is_complete(self) -> bool:
        """ returns a bool of if all data needed to execute a program is present

        :return: is_complete: bool, all information is present to run the program.
        """
        # for attributes in vars(self):

        mapping_dict = {"creation_date": lambda x: x is None,
                        "payload": lambda x: x.empty,
                        "duration": lambda x: x is None,
                        "user_verification": x}

        pass

    def _default_dict_type(self):
            """Literal for """