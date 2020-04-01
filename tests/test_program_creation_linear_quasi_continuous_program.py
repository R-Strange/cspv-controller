import unittest
from unittest import mock
from program_creation import LinearQuasiContinuousProgram, search_for_dangerous_pressures


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
    def test_validate_duration_sad_long(self, mock_input):
        with self.assertWarns(UserWarning) as cm:
            self.linear_quasi_continuous_program.get_program_parameters()

        self.assertEqual(str(cm.warning), "Warning: the duration specified is 57 days. Is this correct?")

    @mock.patch("builtins.input", side_effect=[0.1, 200.0, 100.0])
    def test_validate_duration_sad_short(self, mock_input):
        with self.assertRaises(ValueError) as cm:
            self.linear_quasi_continuous_program.get_program_parameters()

        self.assertEqual(str(cm.exception), "Error: duration expected as a non-negative, non-zero int.")

    @mock.patch("builtins.input", side_effect=[-1, 200.0, 100.0])
    def test_validate_duration_sad_negative(self, mock_input):
        with self.assertRaises(ValueError) as cm:
            self.linear_quasi_continuous_program.get_program_parameters()

        self.assertEqual(str(cm.exception), "Error: duration expected as a non-negative, non-zero int.")

    @mock.patch("builtins.input", side_effect=[10000, 260.0, 100.0])
    def test_validate_pressure_sad_long(self, mock_input):
        with self.assertWarns(UserWarning) as cm:
            self.linear_quasi_continuous_program.get_program_parameters()

        self.assertEqual(str(cm.warning), "Warning: the pressure specified is above 250MPa.")

    @mock.patch("builtins.input", side_effect=[10000, 0.8, 100.0])
    def test_validate_pressure_sad_short(self, mock_input):
        with self.assertRaises(ValueError) as cm:
            self.linear_quasi_continuous_program.get_program_parameters()

        self.assertEqual(str(cm.exception), "Error: pressure expected as a non-negative, non-zero float.")

    @mock.patch("builtins.input", side_effect=[10000, -1, 100.0])
    def test_validate_pressure_sad_negative(self, mock_input):
        with self.assertRaises(ValueError) as cm:
            self.linear_quasi_continuous_program.get_program_parameters()

        self.assertEqual(str(cm.exception), "Error: pressure expected as a non-negative, non-zero float.")

    @mock.patch("builtins.input", side_effect=[1000, 150, 200])
    def test_check_start_and_end_pressure_sad_inverted(self, mock_input):
        with self.assertWarns(UserWarning) as cm:
            self.linear_quasi_continuous_program.get_program_parameters()

        self.assertEqual(str(cm.warning), "Warning: The start pressure is lower than the end pressure.")

    @mock.patch("builtins.input", side_effect=[100, 250, 200])
    def test_search_for_dangerous_pressures_happy(self, mock_input):
        self.linear_quasi_continuous_program.get_program_parameters()
        self.linear_quasi_continuous_program.calculate_program_waypoints()

        self.assertTrue(self.linear_quasi_continuous_program.within_pressure_range)

    @mock.patch("builtins.input", side_effect=[100, 250, 200])
    def test_search_for_dangerous_pressures_sad(self, mock_input):
        self.linear_quasi_continuous_program.get_program_parameters()
        program_df = self.linear_quasi_continuous_program.calculate_program_waypoints()

        program_df.iloc[2, 0] = 1000000

        with self.assertRaises(ValueError) as cm:
            search_for_dangerous_pressures(program_df)

        self.assertEqual(str(cm.exception), "Pressures exceeding safe limits in program.")




if __name__ == "__main__":
    unittest.main()
