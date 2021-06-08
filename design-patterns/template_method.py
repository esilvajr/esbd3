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
