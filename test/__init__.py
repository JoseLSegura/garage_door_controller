import unittest


class TestCase(unittest.TestCase):
    def assertPinStates(self, pin, expected_states):
        pin.assert_states(expected_states)
        self.assertEqual(len(pin.states), len(expected_states))
