from abc import ABC, abstractmethod

# ۱. تعریف کلاس پایه برای دستگاه تهویه

class ClimateControlSystem(ABC):

    @abstractmethod

    def control(self):

        pass

# ۲. کلاس‌های مختلف برای هر نوع دستگاه
class Cooler(ClimateControlSystem):
    def control(self):
        return "Cooling the house"

class Heater(ClimateControlSystem):
    def control(self):
        return "Heating the house"

class Dehumidifier(ClimateControlSystem):
    def control(self):
        return "Dehumidifying the air"

# ۳. کلاس‌های کارخانه‌ای برای هر نوع دستگاه
class CoolerFactory:
    def create_device(self) -> ClimateControlSystem:
        return Cooler()

class HeaterFactory:
    def create_device(self) -> ClimateControlSystem:
        return Heater()

class DehumidifierFactory:
    def create_device(self) -> ClimateControlSystem:
        return Dehumidifier()

# ۴. تابعی برای انتخاب کارخانه مناسب بر اساس شرایط
def get_climate_control_factory(temperature, humidity):
    if temperature > 24:
        return CoolerFactory()
    elif temperature < 24:
        return HeaterFactory()
    elif humidity > 50:
        return DehumidifierFactory()