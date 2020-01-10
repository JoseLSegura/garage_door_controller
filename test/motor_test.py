from unittest import TestCase
from unittest.mock import patch

from gpiozero import Device
from gpiozero.pins.mock import MockFactory, MockPin

from garage_door_controller import Motor


Device.pin_factory = MockFactory(pin_class=MockPin)


class MotorTestCase(TestCase):
    def setUp(self):
        self.sut = Motor(5, 6)
        self.mock_open_pin = self.sut[0].pin
        self.mock_close_pin = self.sut[1].pin
        self.mock_open_pin.clear_states()
        self.mock_close_pin.clear_states()

    def tearDown(self):
        del self.sut

    @patch('time.sleep', lambda _: None)
    def test_open(self):
        self.sut.open_door()
        self.mock_open_pin.assert_states([True, False, True])
        self.assertEqual(len(self.mock_open_pin.states), 3)
        self.mock_close_pin.assert_states([True])
        self.assertEqual(len(self.mock_close_pin.states), 1)
