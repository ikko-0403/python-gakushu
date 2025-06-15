class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run()
print('###############################')
toyotacar = ToyotaCar()
toyotacar.run()
print("################################")
teslacar = TeslaCar()
teslacar.run()
teslacar.auto_run()