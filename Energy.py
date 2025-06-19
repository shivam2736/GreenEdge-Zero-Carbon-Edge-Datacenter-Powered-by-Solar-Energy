# battery_manager.py
class BatteryManager:
    def __init__(self, capacity_kwh=10):
        self.capacity_kwh = capacity_kwh
        self.charge_level = capacity_kwh  # kWh

    def discharge(self, load_kw, duration_hours):
        energy_needed = load_kw * duration_hours
        if energy_needed <= self.charge_level:
            self.charge_level -= energy_needed
            print(f"Battery discharged {energy_needed} kWh, remaining: {self.charge_level} kWh")
            return True
        else:
            print("Insufficient battery charge!")
            return False

    def charge(self, energy_kwh):
        self.charge_level += energy_kwh
        if self.charge_level > self.capacity_kwh:
            self.charge_level = self.capacity_kwh
        print(f"Battery charged to {self.charge_level} kWh")

if __name__ == "__main__":
    battery = BatteryManager()
    battery.discharge(2, 1)
    battery.charge(1.5)
