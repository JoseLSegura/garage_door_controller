from unittest import TestCase
from unittest.mock import patch

from gpiozero import Device
from gpiozero.pins.mock import MockFactory, MockPin

from garage_door_controller import ElectricLock


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
        self.pin.assert_states([True])
        self.assertEqual(len(self.pin.states), 1)

    def test_disabled_method_off(self):
        initial_value = self.sut.value
        self.sut.off()
        self.assertEqual(initial_value, self.sut.value)
        self.pin.assert_states([True])
        self.assertEqual(len(self.pin.states), 1)

    @patch('time.sleep', lambda _: None)
    def test_open(self):
        self.sut.open()
        self.sut.pin.assert_states([True, False, True])
        self.assertEqual(len(self.pin.states), 3)
