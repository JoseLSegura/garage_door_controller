import time

from gpiozero import CompositeDevice

from .electric_lock import ElectricLock
from .motor import Motor


class GarageDoor(CompositeDevice):
    def __init__(self, electrick_lock_pin, open_pin, close_pin, active_high=False, pin_factory=None):
        self.motor = Motor(open_pin, close_pin, active_high=active_high, pin_factory=pin_factory)
        self.lock = ElectricLock(electrick_lock_pin, pin_factory=pin_factory)

        super().__init__(self.motor, self.lock)

    def open_door(self):
        self.lock.open()
        time.sleep(1)

        self.motor.open_door()

    def close_door(self):
        self.motor.close_door()
