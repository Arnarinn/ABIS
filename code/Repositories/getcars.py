from .formatdata import formatData
from Models.car import Car
import csv

class GetCars:
    def carData(self):
        formattedData = formatData(open('../data/cars.csv'))
        carObjectArray = []
        for line in formattedData:
            carObjectArray.append(Car(line[0], line[1], line[2], line[3], line[4],
                                      line[5], line[6], line[7], line[8], line[9],
                                      line[10], line[11], line[12], line[13]))
        return carObjectArray




     # Writes all cars down to the cars.csv file
    def carInsert(self, carList):
        with open('../data/cars.csv', 'w', newline = '') as carFile:
            carFileWriter = csv.writer(carFile)
            # This is the headder
            carFileWriter.writerow(['manufacturer', 'color', 'cost',\
                                         'license plate', 'distance', 'year',\
                                         'car', 'type', 'number of seats',\
                                         'number of doors', 'inspected', 'fuel',\
                                         'wheel drive', 'shifting option', 'status'])
            for obj in carList:
                carFileWriter.writerow(obj.dataList())