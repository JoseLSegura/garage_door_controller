import asyncio

from gpiozero import CompositeDevice, DigitalOutputDevice


class AsyncMotor(CompositeDevice):
    def __init__(self, open_pin, close_pin, open_time, close_time,
                 active_high=False, pin_factory=None):
        self.open_door_relay = DigitalOutputDevice(
            open_pin, active_high=active_high, initial_value=0, pin_factory=pin_factory)
        self.close_door_relay = DigitalOutputDevice(
            close_pin, active_high=active_high, initial_value=0, pin_factory=pin_factory)

        super().__init__(self.open_door_relay, self.close_door_relay)
        self.open_move_duration = open_time
        self.close_move_duration = close_time

    async def open_door(self):
        self.close_door_relay.off()
        await asyncio.sleep(1)
        self.open_door_relay.on()
        await asyncio.sleep(self.open_move_duration)
        self.open_door_relay.off()

    async def close_door(self):
        self.open_door_relay.off()
        await asyncio.sleep(1)
        self.close_door_relay.on()
        await asyncio.sleep(self.close_move_duration)
        self.close_door_relay.off()
