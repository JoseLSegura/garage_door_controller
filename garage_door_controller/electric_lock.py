import time

from gpiozero import DigitalOutputDevice


class ElectricLock(DigitalOutputDevice):
    def __init__(self, pin, pin_factory=None):
        super().__init__(
            pin, active_high=False, initial_value=False,
            pin_factory=pin_factory)

        self.on = self.off = self.blink = lambda: None

    def open(self):
        super().on()
        time.sleep(0.5)
        super().off()
