class Car(object):
    def __init__(self, model=None):
        self.model = model 
    def run(self):# これで model をインスタンス変数として保持
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        #self.model = model
        super().__init__(model)#親変数のものにあやかる
        self._enable_auto_run = enable_auto_run
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

car = Car()
car.run()
print('###############################')
toyotacar = ToyotaCar('lexus')
print(toyotacar.model)
toyotacar.run()
print("################################")
teslacar = TeslaCar('Model S')
print(teslacar.model)
teslacar.run()
teslacar.auto_run()