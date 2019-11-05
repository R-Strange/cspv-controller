import unittest
from unittest import mock
from program_creation import LinearQuasiContinuousProgram


class TestLinearQuasiContinuousProgram(unittest.TestCase):
    def setUp(self) -> None:
        self.linear_quasi_continuous_program = LinearQuasiContinuousProgram()

    def test_init(self):
        self.assertSequenceEqual(
            [int(), float(), float()],
            [
                self.linear_quasi_continuous_program.duration,
                self.linear_quasi_continuous_program.starting_pressure,
                self.linear_quasi_continuous_program.ending_pressure,
            ],
        )

    @mock.patch("builtins.input", side_effect=[5000000, 200.0, 100.0])
    def test_validate_duration_sad(self, mock_input):
        with self.assertWarns(UserWarning) as cm:
            self.linear_quasi_continuous_program.get_program_parameters()

        self.assertEqual(str(cm.warning), "Warning: the duration specified is 57 days. Is this correct?")



if __name__ == "__main__":
    unittest.main()
