import time

from gpiozero import CompositeDevice, DigitalOutputDevice


class Motor(CompositeDevice):
    TIME_TO_STOP = 7

    def __init__(self, open_pin, close_pin, active_high=False, pin_factory=None,
                 time_to_stop=Motor.TIME_TO_STOP):
        self.open_door_relay = DigitalOutputDevice(
            open_pin, active_high=active_high, initial_value=0, pin_factory=pin_factory)
        self.close_door_relay = DigitalOutputDevice(
            close_pin, active_high=active_high, initial_value=0, pin_factory=pin_factory)
        self.time_to_stop = time_to_stop

        super().__init__(self.open_door_relay, self.close_door_relay)

    def open_door(self):
        self.close_door_relay.off()
        time.sleep(1)
        self.open_door_relay.on()
        time.sleep(self.time_to_stop)
        self.open_door_relay.off()

    def close_door(self):
        self.open_door_relay.off()
        time.sleep(1)
        self.close_door_relay.on()
        time.sleep(self.time_to_stop)
        self.close_door_relay.off()
