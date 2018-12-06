#File for making tests in the code

from UI.carui import CarUi

test = CarUi()
print('\n Unavailable:')
test.dispUnavailableCars()
print('\n Available:')
test.dispAvailableCars()