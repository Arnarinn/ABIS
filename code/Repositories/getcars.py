from .formatdata import formatData


class GetCars:
    def carData(self):
        return formatData(open('data/cars.csv'))
