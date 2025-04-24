## class abstract adalah blueprint dari class
## abc = abstract base class
from abc import ABC,abstractmethod

class Button(ABC):

    @abstractmethod
    def click(self):
        pass ## sengaja kosong supaya di implenetasikan di subclass 


class PushButton(Button):

    def click(self):
        print("push button click")


class RadioButton(Button):
    def click(self):
        print("radio button click")


tombol1 = PushButton()
tombol2 = RadioButton()
tombol3 = Button()

tombol1.click()
tombol2.click()
# tombol3.click() ## akan error(gabisa langsung diakses)


