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