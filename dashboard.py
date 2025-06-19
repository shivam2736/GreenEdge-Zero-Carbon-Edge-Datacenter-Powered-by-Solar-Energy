# dashboard.py
class Dashboard:
    def __init__(self, solar_monitor, battery_manager):
        self.solar_monitor = solar_monitor
        self.battery_manager = battery_manager

    def display_status(self):
        v, c, p = self.solar_monitor.read_sensors()
        charge = self.battery_manager.charge_level
        print(f"Solar Power: {p} W (V: {v} V, I: {c} A)")
        print(f"Battery Charge Level: {charge} kWh")

if __name__ == "__main__":
    from solar_monitor import SolarMonitor
    from battery_manager import BatteryManager

    sm = SolarMonitor()
    bm = BatteryManager()
    dash = Dashboard(sm, bm)
    dash.display_status()
