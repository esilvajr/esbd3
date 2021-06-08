## Design Patterns

#### Singleton

```python
class Singleton:

    _instance = None
    
    @classmethod
    def instance(cls): #cls == class
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

```

#### Strategy
```python
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

```

#### Facade
```python
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

```

#### Adapter
```python
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

```

#### Factory Method
```python
class Product: 
    def doStuff(self) -> None:
        raise NotImplementedError 

class ConcreteProduct(Product):
    def doStuff(self) ->  None:
        pass

class Creator:
    def factoryMethod(self) -> Product:
        raise NotImplementedError

    def createProduct(self) -> None:
        product = self.factoryMethod()
        product.doStuff()

class ConcreteCreator(Creator):
    def factoryMethod(self) -> Product:
        return ConcreteProduct()

```

#### State
```python

```

#### Observer
```python
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


```

#### Template Method
```python
class AbstractClass():

    def template_method(self) -> None:
        self.required_operations1()
        self.required_operations2()

    @staticmethod
    def primitiveOperations1(self) -> None:
        pass

    @staticmethod
    def primitiveOperations2(self) -> None:
        pass


class ConcreteClassA(AbstractClass):
    def primitiveOperations1(self) -> None:
        pass

    def primitiveOperations2(self) -> None:
        pass

def clientCode(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()

```


### Referências

#### Livros
- Padrões de Projetos: Soluções Reutilizáveis de Software Orientados a Objetos. Gamma, E. [Livro]
- Mergulho nos Padrões de Projeto. Shvets, A. [Livro]

#### Web
- http://refactoring.guru/pt-br/design-patterns/
- https://github.com/kamranahmedse/design-patterns-for-humans
- https://designpatternsphp.readthedocs.io/
