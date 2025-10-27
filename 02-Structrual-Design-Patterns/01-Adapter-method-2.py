class EuropeanSocket:
    def provide_electricity(self):
        return "220V"

class AmericanSocket:
    def provide_electricity(self):
        return "110V"

class AmericanDevice:
    def plug_in(self, socket: AmericanSocket):
        if socket.provide_electricity() == "110V":
            print("Device is working!")
        else:
            print("Device is not working!")

class EuropeanToAmericanAdapter(AmericanSocket):
    def __init__(self, european_socket: EuropeanSocket):
        self.european_socket = european_socket

    def provide_electricity(self):
        voltage = self.european_socket.provide_electricity()
        if voltage == "220V":
            return "110V"
        return voltage


if __name__ == "__main__":

    european_socket = EuropeanSocket()
    american_device = AmericanDevice()

    american_device.plug_in(european_socket)

    adapter = EuropeanToAmericanAdapter(european_socket)
    american_device.plug_in(adapter)