class Car:
    
    count=0
    
    def __init__(self, make, model, price, segments = "Exonomy"):
        Car.count += 1
        self._make = make
        self._model = model
        self._price = price
        self._segments = segments

    def calculate_premium(self, tenure):
        if self._segment == "Economy":
            return tenure*self._price*0.15
        else:
            return tenure*self._price*0.20

    @staticmethod
    def show_count():
        print(f'Total cars : {Car.count}')

    def __str__(self):
        return (f'Car Data : {self._make} - {self._model},'
               f'{self._price},{self._segment}')
        
    def __repr__(self):
        return (f'Car({self._make} - {self._model},'
               f'{self._price},{self._segment})')