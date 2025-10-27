class PlumbingSystem:
    def __init__(self):
        self.pressure = 0

    def set_pressure(self, pressure):
        self.pressure = pressure
        print(f"PlumbingSystem: Water pressure set to {self.pressure} PSI.")

    def turn_on(self):
        print("PlumbingSystem: Water system turned on.")

    def turn_off(self):
        print("PlumbingSystem: Water system turned off.")

class ElectricalSystem:
    def __init__(self):
        self.voltage = 0

    def set_voltage(self, voltage):
        self.voltage = voltage
        print(f"ElectricalSystem: Voltage set to {self.voltage} volts.")

    def turn_on(self):
        print("ElectricalSystem: Electrical system turned on.")

    def turn_off(self):
        print("ElectricalSystem: Electrical system turned off.")

class House:
    def __init__(self):
        self.plumbing_system = PlumbingSystem()
        self.electrical_system = ElectricalSystem()

    def turn_on_systems(self):
        print("House: Turning on all systems...")
        self.plumbing_system.set_pressure(50)
        self.plumbing_system.turn_on()
        self.electrical_system.set_voltage(220)
        self.electrical_system.turn_on()
        print("House: All systems are now on.")

    def shutdown_systems(self):
        print("House: Shutting down all systems...")
        self.plumbing_system.turn_off()
        self.electrical_system.turn_off()
        print("House: All systems are now off.")

# استفاده از کلاس House
if __name__ == "__main__":
    house = House()

    # روشن کردن سیستم‌ها
    house.turn_on_systems()

    # خاموش کردن سیستم‌ها
    house.shutdown_systems()