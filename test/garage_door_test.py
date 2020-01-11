from unittest import TestCase
from unittest.mock import patch

from gpiozero import Device
from gpiozero.pins.mock import MockFactory, MockPin

from garage_door_controller import GarageDoor


Device.pin_factory = MockFactory(pin_class=MockPin)


class MotorTestCase(TestCase):
    def setUp(self):
        self.sut = GarageDoor(1, 2, 3)
        self.motor = self.sut[0]
        self.lock = self.sut[1]

    def tearDown(self):
        del self.sut

    @patch('time.sleep', lambda _: None)
    def test_open_door(self):
        self.sut.open_door()

        mock_pin_open = self.motor[0].pin
        mock_pin_close = self.motor[1].pin
        mock_pin_lock = self.lock.pin
