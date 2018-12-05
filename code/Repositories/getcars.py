from .formatdata import formatData
from Models.car import Car

class GetCars:
    def carData(self):
        formattedData = formatData(open('../data/cars.csv'))
        carObjectArray = []
        for line in formattedData:
            carObjectArray.append(Car(line[0], line[1], line[2], line[3], line[4],
                                      line[5], line[6], line[7], line[8], line[9],
                                      line[10], line[11], line[12], line[13]))
        return carObjectArray
