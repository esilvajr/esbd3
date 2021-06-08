class Subject():

    def attach(self, observer: Observer) -> None:
        raise NotImplementedError

    def detach(self, observer: Observer) -> None:
        raise NotImplementedError

    def notify(self) -> None:
        raise NotImplementedError


class ConcreteSubject(Subject):

    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        self.notify()


class Observer():

    def update(self, subject: Subject) -> None:
        raise NotImplementedError

class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 0:
            pass

class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state >= 0:
            pass
