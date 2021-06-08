class Store():
    def attach(self) -> None:
        raise NotImplemetedError
    def detach(self) -> None:
        raise NotImplemetedError
    def notify(self) -> None:
        raise NotImplemetedError

class AppleStore(Store):
    
    _iphoneState: int = 0

    _observers: List[CustomerObserver] = []

    def attach(self, observer: CustomerObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: CustomerObserver) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.sendEmail(self)
            observer.sendWhatsapp(self)

    def setIphones(self, quantity: int) -> None:
        self._iphoneState = quantity
        self.notify()

class CustomerObserver():
    def sendEmail(self, subject: Store):
        raise NotImplemetedError

    def sendWhatsapp(self, subject: Store):
        raise NotImplemetedError

class IphoneCustomerObserver(CustomerObserver):
    def sendEmail(self, subject: Store):
        if subject._iphoneState >= 1:
            email.send()

    def sendWhatsapp(self, subject: Store):
        if subject._iphoneState >= 1 and suject._iphoneState <= 10:
            mobile.whatsapp().send()

if __name__ == "__main__":

    vemIphoneVemObserver = IphoneCustomerObserver()
    
    appleStore = AppleStore()
    appleStore.attach(vemIphoneVemObserver)
    appleStore.setIphones(100)