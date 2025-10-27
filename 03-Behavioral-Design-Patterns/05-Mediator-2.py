class TrafficMediator:
    def __init__(self):
        self._lights = []

    def register_light(self, light):
        self._lights.append(light)

    def notify(self, sender, event):
        if event == "green":
            for light in self._lights:
                if light != sender:
                    light.turn_red()

class TrafficLight:
    def __init__(self, name, mediator):
        self._name = name
        self._mediator = mediator
        self._mediator.register_light(self)
        self._state = "red"

    def turn_green(self):
        if self._state != "green":
            print(f"{self._name} turns green.")
            self._state = "green"
            self._mediator.notify(self, "green")

    def turn_red(self):
        if self._state != "red":
            print(f"{self._name} turns red.")
            self._state = "red"


if __name__ == "__main__":
    mediator = TrafficMediator()

    light1 = TrafficLight("Light 1", mediator)
    light2 = TrafficLight("Light 2", mediator)
    light3 = TrafficLight("Light 3", mediator)

    light1.turn_green()
    light2.turn_green()
    light3.turn_green()
