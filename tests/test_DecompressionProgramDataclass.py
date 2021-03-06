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

    def test_datatype_check_sad(self):
        self.DecompressionProgram.duration = "long time"

        self.assertFalse(self.DecompressionProgram.datatype_check()[0])

    def test_datatype_check_happy(self):
        self.DecompressionProgram.creation_date = datetime.datetime.now()
        self.DecompressionProgram.payload = pd.DataFrame(np.random.randint(0, 100, size=(100, 2)),
                                                         columns=['time', 'pressure'])
        self.DecompressionProgram.duration = 100

        self.assertTrue(self.DecompressionProgram.datatype_check()[0])

    def test_completion_test_happy(self):
        self.DecompressionProgram.creation_date = datetime.datetime.now()
        self.DecompressionProgram.payload = pd.DataFrame(np.random.randint(0, 100, size=(100, 2)),
                                                         columns=['time', 'pressure'])
        self.DecompressionProgram.duration = 100

        self.DecompressionProgram.user_verification = True

        self.assertTrue(self.DecompressionProgram.completion_check())

    def test_completion_test_sad(self):
        self.DecompressionProgram.creation_date = datetime.datetime.now()
        self.DecompressionProgram.payload = pd.DataFrame(np.random.randint(0, 100, size=(100, 2)),
                                                         columns=['time', 'pressure'])
        self.DecompressionProgram.duration = 100

        self.DecompressionProgram.user_verification = False

        self.assertFalse(self.DecompressionProgram.completion_check())


if __name__ == '__main__':
    unittest.main()
