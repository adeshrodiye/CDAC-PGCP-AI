class Car:
    count = 0
    def __init__(self,make,model,price,segment="Economy"):
        Car.count +=1
        self._make = make
        self._model = model
        self._price = price
        self._segment = segment

    def calculate_premium(self,tenure):
        if self._segment == "Economy":
            return tenure + self._price*0.15
        else:
            return tenure + self._price * 0.20

    @property
    def make(self):
        return self._make

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("Price cannot be negative")

    @staticmethod
    def show_count():
        print(f"Total cars: {Car.count}")

    @classmethod
    def set_count(cls):
        count = 100

    @classmethod
    def from_string(cls,data):
        make, model , price = data.split(',')
        return cls(make,model,int(price))


    def __str__(self):
        return (f"Car Data : {self._make} - {self._model} -"
                f"{self._price} - {self._segment}")


    def __repr__(self):
        return (f"Car( {repr(self._make)},{repr(self._model)},"
                f"{repr(self._price)},{repr(self._segment)})")