from abc import ABC, abstractmethod

# تعریف رابط برای وضعیت‌های مختلف
class State(ABC):
    @abstractmethod
    def think(self):
        pass

# پیاده‌سازی حالت خوشحالی
class Happy(State):
    def think(self):
        return "Everything is great! I'm feeling positive and optimistic."

# پیاده‌سازی حالت غمگینی
class Sad(State):
    def think(self):
        return "I'm feeling down. Everything seems gloomy and hard."

# پیاده‌سازی حالت عصبانیت
class Angry(State):
    def think(self):
        return "I'm frustrated and angry. Everything is annoying me right now."

# کلاس Human که وضعیت را مدیریت می‌کند
class Human:
    def __init__(self, state: State):
        self.state = state

    def set_state(self, state: State):
        self.state = state

    def think(self):
        return self.state.think()

# استفاده از کد
if __name__ == "__main__":
    # ایجاد یک فرد با وضعیت اولیه خوشحالی
    person = Human(Happy())
    print(person.think())

    # تغییر وضعیت به غمگینی
    person.set_state(Sad())
    print(person.think())

    # تغییر وضعیت به عصبانیت
    person.set_state(Angry())
    print(person.think())