class Soldier:
    def __init__(self, type, power):
        self._type = type
        self._power = power

    def get_type(self):
        return self._type

    def get_power(self):
        return self._power


class SoldierFactory:
    _soldiers = {}

    @classmethod
    def get_soldier(cls, type, power):
        key = (type, power)
        if key not in cls._soldiers:
            cls._soldiers[key] = Soldier(type, power)
        return cls._soldiers[key]


if __name__ == "__main__":
    archer1 = SoldierFactory.get_soldier("Archer", 20)
    archer2 = SoldierFactory.get_soldier("Archer", 20)
    barbarian1 = SoldierFactory.get_soldier("Barbarian", 30)

    print(f"Archer1: Type = {archer1.get_type()}, Power = {archer1.get_power()}")
    print(f"Archer2: Type = {archer2.get_type()}, Power = {archer2.get_power()}")
    print(f"Barbarian1: Type = {barbarian1.get_type()}, Power = {barbarian1.get_power()}")

    print(f"Archer1 and Archer2 are the same instance: {archer1 is archer2}")
