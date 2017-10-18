import time
import lifepo4weredPyController


@lifepo4weredPyController.battery.observeState()
def printState(previous, actual):
    print("previously:{0}, now:{1}".format(previous, actual))


try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    myLifepo4wered.ceaseReading()
    print('stopped!')
