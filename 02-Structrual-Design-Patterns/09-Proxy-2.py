class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access before firing a request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

if __name__ == "__main__":
    real_subject = RealSubject()
    real_subject.request()

    proxy = Proxy(real_subject)
    proxy.request()