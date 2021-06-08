class Strategy:
    def behavior(self) -> None:
        raise NotImplementedError

class ConcreteStrategyA(Strategy):
    def behavior(self) -> None:
        pass

class ConcreteStrategyB(Strategy):
    def behavior(self) -> None:
        pass

class Context():

    _strategy: Strategy

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def method(self) -> None:
        self._strategy.behavior()