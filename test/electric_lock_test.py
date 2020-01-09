from unittest import TestCase

from gpiozero import Device
from gpiozero.pins.mock import MockFactory, MockPin

from garage_door_controller import ElectricLock


Device.pin_factory = MockFactory(pin_class=MockPin)


class ElectricLockTestCase(TestCase):
    def test_disabled_methods(self):
        sut = ElectricLock(4, initial_value=0)
        initial_value = sut.value
        sut.on()
        self.assertEqual(initial_value, sut.value)

        del sut
        sut = ElectricLock(4, initial_value=1)
        initial_value = sut.value
        sut.off()
        self.assertEqual(initial_value, sut.value)

    def test_open(self):
        sut = ElectricLock(4)
        sut.open()
