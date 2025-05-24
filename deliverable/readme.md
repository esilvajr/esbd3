## Deliverable [Elevator Schema]

Resolução do exercicio proposto dos padrões em um cenário de elevadores.

![Elevator](elevator_diagram.drawio.svg)

#### State 
Implementação dos estados do elevador, sendo eles:
- Subindo;
- Descendo;
- Emperrado;
- Em manutenção.


```python

class State():

    def pressingGoingUpButton(self) -> None:
        raise NotImplementedError

    def pressingGoingDownButton(self) -> None:
        raise NotImplementedError

    def pressingEmergencyButton(self) -> None:
        raise NotImplementedError


class GoingUpState(State):

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls
        return cls._instance

    def pressingGoingUpButton(self) -> None:
        pass

    def pressingGoingDownButton(self) -> None:
        pass

    def pressingEmergencyButton(self) -> None:
        pass


class GoingDownState(State):

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls
        return cls._instance

    def pressingGoingUpButton(self) -> None:
        pass

    def pressingGoingDownButton(self) -> None:
        pass

    def pressingEmergencyButton(self) -> None:
        pass


class EmergencyState(State):

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls
        return cls._instance

    def pressingGoingUpButton(self) -> None:
        pass

    def pressingGoingDownButton(self) -> None:
        pass

    def pressingEmergencyButton(self) -> None:
        pass


class MaintenceState(State):

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls
        return cls._instance

    def pressingGoingUpButton(self) -> None:
        pass

    def pressingGoingDownButton(self) -> None:
        pass

    def pressingEmergencyButton(self) -> None:
        pass  

```

#### Observers 
Implementação dos observadores do elevador, sendo eles:
- Outros, como subindo e descendo;
- Manutenção;
- Entretenimento;
- e Emergência.

```python
class Observer():
    
    def performService(self) -> None:
        raise NotImplementedError
    
class OtherServiceObserver(Observer):
    
    def performService(self, state: State) -> None:
        if isinstance(state, GoingUpState) or isinstance(state, GoingDownState):
            pass
  
class MaintenceServiceObserver(Observer):
    
    def performService(self, state: State) -> None:
        if isinstance(state, MaintenceState):
            pass
    
class EntertainmentServiceObserver(Observer):
    
    def performService(self, state: State) -> None:
        if isinstance(state, GoingUpState) or isinstance(state, GoingDownState):
            pass

class EmergencyServiceObserver(Observer):     
    
    def performService(self, state: State) -> None:
        if isinstance(state, EmergencyState):
            pass
    
class Subject():
    
    __observers: List[Observer] = []
    
    def attach(self, observer: Observer)-> None:
        self.__observers.append(observer)
        
    def detach(self, observer: Observer)-> None:
        self.__observers.remove(observer)
        
    def notify(self, state: State)-> None:
        for observer in self.__observers:
            observer.performService(state)

```


#### Factories 
Implementação das fábricas do elevador, sendo eles:
- Serviço;
- e Social.

```python
class ElevatorFactory():

    def createElevator(self) -> Elevator:
        raise NotImplementedError


class SocialElevatorFactory(ElevatorFactory):

    def createElevator(self) -> SocialElevator:
        return SocialElevator.getInstance()


class ServiceElevatorFactory(ElevatorFactory):

    def createElevator(self) -> ServiceElevator:
        return ServiceElevator.getInstance()

```

#### Classes e Objetos 
Implementação das classes e objetos do elevador, sendo eles:
- Elevador;
- Elevador social;
- e Elevador de serviço

```python
class Elevator(Subject):
    __instance = None
    __currentState: State

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def setState(self, state: State) -> None:
        self.__currentState = state

    def getState(self) -> State:
        return self.__currentState


class SocialElevator(Elevator):

    def startGoingUp(self):
        self.setState(GoingUpState())
        self.notify(self.getState())

    def startGoingDown(self):
        self.setState(GoingDownState())
        self.notify(self.getState())

    def startEmergencyMode(self):
        self.setState(EmergencyState())
        self.notify(self.getState())


class ServiceElevator(Elevator):

    def startGoingUp(self):
        self.setState(GoingUpState())
        self.notify(self.getState())

    def startGoingDown(self):
        self.setState(GoingDownState())
        self.notify(self.getState())

    def startEmergencyMode(self):
        self.setState(EmergencyState())
        self.notify(self.getState())


```

#### Main

Exemplo de execução:

```python
if __name__ == "__main__":
   
   elevator1 = SocialElevatorFactory().createElevator()
   elevator2 = ServiceElevatorFactory().createElevator()
   
   elevator1.attach(MaintenceServiceObserver())
   elevator1.attach(OtherServiceObserver())
   
   elevator1.startGoingUp()
   
   elevator2.attach(OtherServiceObserver())
   elevator2.attach(EmergencyServiceObserver())
   
   elevator2.startEmergencyMode()
   
```
