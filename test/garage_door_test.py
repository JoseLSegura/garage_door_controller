from unittest.mock import patch

from gpiozero import Device
from gpiozero.pins.mock import MockFactory, MockPin

from garage_door_controller import GarageDoor

from . import TestCase


Device.pin_factory = MockFactory(pin_class=MockPin)


class MotorTestCase(TestCase):
    def setUp(self):
        self.sut = GarageDoor(1, 2, 3)
        self.motor = self.sut[0]
        self.lock = self.sut[1]

        self.motor[0].pin.clear_states()
        self.motor[1].pin.clear_states()
        self.lock.pin.clear_states()

    def tearDown(self):
        del self.sut

    @patch('time.sleep', lambda _: None)
    def test_open_door(self):
        self.sut.open_door()

        mock_pin_open = self.motor[0].pin
        mock_pin_close = self.motor[1].pin
        mock_pin_lock = self.lock.pin

        self.assertPinStates(mock_pin_lock, [True, False, True])
        self.assertPinStates(mock_pin_open, [True, False, True])
        self.assertPinStates(mock_pin_close, [True])

    @patch('time.sleep', lambda _: None)
    def test_close_door(self):
        self.sut.close_door()

        mock_pin_open = self.motor[0].pin
        mock_pin_close = self.motor[1].pin
        mock_pin_lock = self.lock.pin

        self.assertPinStates(mock_pin_lock, [True])
        self.assertPinStates(mock_pin_open, [True])
        self.assertPinStates(mock_pin_close, [True, False, True])
