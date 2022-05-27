import random

class RouteStrategy():
    def getRoute() -> str:
        raise NotImplementedError

class NotSafeRoute(RouteStrategy):
    def isSafe(self) -> bool:
        return random.choice([True, False])

    def getRoute(self) -> str:
        return "The shortest route is safe by now"

class SafeRoute(RouteStrategy):
    def isSafe(self) -> bool:
        return random.choice([True, False])

    def getRoute(self) -> str:
        return "The safe route is safe by now"
    
class SuperSafeRoute(RouteStrategy):
    def isSafe(self) -> bool:
        return True

    def getRoute(self) -> str:
        return "The super safe route is the best one"

class Route():
    _strategy: None

    def __init__(self, strategy: RouteStrategy) -> None:
        self._strategy = strategy

    def getStrategy(self) -> RouteStrategy:
        return self._strategy

    def calculateRoute(self) -> None:

        if (self._strategy.isSafe() == True):
            print(self._strategy.getRoute())

        elif(self._strategy.isSafe() == False):

            self._strategy = SafeRoute()
            if (self._strategy.isSafe() == True):
                print(self._strategy.getRoute())

            else:
                self._strategy = SuperSafeRoute()
                print(self._strategy.getRoute())


if __name__ == "__main__":

    route = Route(NotSafeRoute())
    route.calculateRoute()

    print(route.getStrategy())
    


