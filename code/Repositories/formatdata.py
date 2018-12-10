import csv


# Reads the .csv file and returns it as a list
def formatData(file):
    array = []
    with file as dataFile:
        data = csv.reader(dataFile)
        next(data)
        array = list(data)
    return array
