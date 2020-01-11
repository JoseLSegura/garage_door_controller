from unittest.mock import patch

from gpiozero import Device
from gpiozero.pins.mock import MockFactory, MockPin

from garage_door_controller import ElectricLock

from . import TestCase


Device.pin_factory = MockFactory(pin_class=MockPin)


class ElectricLockTestCase(TestCase):
    def setUp(self):
        self.sut = ElectricLock(4)
        self.pin = self.sut.pin
        self.pin.clear_states()

    def tearDown(self):
        del self.sut

    def test_disabled_method_on(self):
        initial_value = self.sut.value
        self.sut.on()
        self.assertEqual(initial_value, self.sut.value)
        self.assertPinStates(self.pin, [True])

    def test_disabled_method_off(self):
        initial_value = self.sut.value
        self.sut.off()
        self.assertEqual(initial_value, self.sut.value)
        self.assertPinStates(self.pin, [True])

    @patch('time.sleep', lambda _: None)
    def test_open(self):
        self.sut.open()
        self.assertPinStates(self.pin, [True, False, True])
