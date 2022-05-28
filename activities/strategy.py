import random

class RouteStrategy():
    def getRoute() -> bool:
        raise NotImplementedError

class NotSafeRoute(RouteStrategy):

    def getRoute(self) -> bool:
        #Pegando comportamento da NotSaferoute
        return random.choice([True, False])

class SafeRoute(RouteStrategy):

    def getRoute(self) -> bool:
        #Pegando comportamento da SafeRoute
        return random.choice([True, False])
    
class SuperSafeRoute(RouteStrategy):

    def getRoute(self) -> bool:
        #Pegando comportamento da SuperSafeRoute
        return True

class Route():
    _strategy: None

    def __init__(self, strategy: RouteStrategy) -> None:
        self._strategy = strategy

    def getStrategy(self) -> RouteStrategy:
        return self._strategy

    def calculateRoute(self) -> bool:
        return self._strategy.getRoute()


if __name__ == "__main__":

    routeA = Route(NotSafeRoute())
    routeB = Route(SafeRoute())
    routeC = Route(SuperSafeRoute())

    if (routeA.calculateRoute()):
        print("Rota mais curta escolhida")

    elif(routeB.calculateRoute()):
        print("Rota média porém segura escolhida")   

    else:
        print("Rota mais longa porém segura escolhida")
            
        



    


