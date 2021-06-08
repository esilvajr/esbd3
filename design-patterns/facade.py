class SubSystemA(): 
    def operation1(self) -> None:
        pass

    def operationZ(self) -> None:
        pass

class SubSystemB():
    def operation2(self) -> None:
        pass

    def operationY(self) -> None:
        pass

class Facade():

    _systemA: None
    _systemB: None

    def __init__(self, systemA: SubSystemA, systemB: SubSystemB) -> None:
        self._systemA = systemA
        self._systemB = systemB


    def operation(self) -> None:
        self._systemA.operation1()
        self._systemA.operationZ()
        self._systemB.operation2()
        self._systemB.operationY()