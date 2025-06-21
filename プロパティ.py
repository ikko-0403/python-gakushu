class Car(object):
    def __init__(self, model=None):
        self.model = model 
    def run(self):# これで model をインスタンス変数として保持
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', 
    enable_auto_run=False,
    passwd='123'):
        #self.model = model
        super().__init__(model)#親変数のものにあやかる
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

#ある条件を満たせば書き換えて良いよ
    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    
    @enable_auto_run.setter
    def enable_auto_run(self, value):
        if self.passwd == '456':
            self._enable_auto_run = value
        else:
            raise ValueError

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')
        
    


print("################################")
teslacar = TeslaCar('Model S', passwd='456')
teslacar.enable_auto_run = True
print(teslacar._enable_auto_run)