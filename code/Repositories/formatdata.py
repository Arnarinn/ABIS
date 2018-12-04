import csv


def formatData(file):
    array = []
    with file as dataFile:
        data = csv.reader(dataFile)
        next(data)
        for line in data:
            array.append(line)
    return array
