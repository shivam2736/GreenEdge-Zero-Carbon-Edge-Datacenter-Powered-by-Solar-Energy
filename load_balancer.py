# load_balancer.py
class LoadBalancer:
    def __init__(self, battery_manager):
        self.battery_manager = battery_manager

    def schedule_task(self, load_kw, duration_hours, priority='normal'):
        if self.battery_manager.charge_level <= 1 and priority != 'high':
            print("Low battery. Postponing non-critical task.")
            return False
        else:
            success = self.battery_manager.discharge(load_kw, duration_hours)
            if success:
                print(f"Task scheduled: {load_kw}kW for {duration_hours}h with priority {priority}")
            return success

if __name__ == "__main__":
    from battery_manager import BatteryManager
    battery = BatteryManager()
    lb = LoadBalancer(battery)
    lb.schedule_task(3, 1, 'normal')
    lb.schedule_task(1, 0.5, 'high')
