import datetime
import unittest

import numpy as np
import pandas as pd

import DecompressionProgramDataclass


class TestDecompressionProgram(unittest.TestCase):
    def setUp(self):
        self.DecompressionProgram = DecompressionProgramDataclass.DecompressionProgram(
            creation_date=datetime.datetime(2019, 1, 1, 1, 1, 1, 1),
            payload=pd.DataFrame(),
            duration=0,
            user_verification=False,
            type_of_program="__init__"
        )

    def test_set_values_happy(self):
        self.DecompressionProgram.duration = 10

        self.assertEqual(self.DecompressionProgram.duration, 10)

    def test_dtypes_check_sad(self):

        output = self.DecompressionProgram.dtypes_check()

        self.assertTrue(output.is_correct)

    def test_dtypes_check_happy(self):

        self.DecompressionProgram.creation_date = datetime.datetime.now()
        self.DecompressionProgram.payload = pd.DataFrame(np.random.randint(0, 100, size=(100, 2)),
                                                         columns=['time', 'pressure'])
        self.DecompressionProgram.duration = 100

        output = self.DecompressionProgram.dtypes_check()

        self.assertTrue(output.is_correct)


if __name__ == '__main__':
    unittest.main()
