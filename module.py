# solar_monitor.py
import random
import time

class SolarMonitor:
    def __init__(self):
        self.voltage = 0.0
        self.current = 0.0
        self.power = 0.0

    def read_sensors(self):
        # Simulate sensor reading
        self.voltage = round(random.uniform(20.0, 24.0), 2)  # Volts
        self.current = round(random.uniform(5.0, 10.0), 2)   # Amps
        self.power = round(self.voltage * self.current, 2)   # Watts
        return self.voltage, self.current, self.power

    def log_power(self):
        v, c, p = self.read_sensors()
        print(f"Voltage: {v}V, Current: {c}A, Power: {p}W")
        # Here you can add code to log to a file or database

if __name__ == "__main__":
    monitor = SolarMonitor()
    while True:
        monitor.log_power()
        time.sleep(5)
