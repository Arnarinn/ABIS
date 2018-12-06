#File for making tests in the code

from Business.cardomain import CarDomain

cars = CarDomain()
cars.setAllAsUnavailable()
#cars.dispAvailableCars()
cars.dispUnavailableCars()