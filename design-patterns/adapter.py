class Target:
    def request(self) -> None:
        raise NotImplementedError

class Adaptee:
    def specificRequest(self) -> None:
        pass

class Adapter(Target):

    _adaptee: None

    def __init__(self, adaptee: Adaptee) -> None:
        self._adaptee = adaptee

    def request(self) -> None:
        self._adaptee.specificRequest()