class Person(object):
    def __init__(self, age=1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('OK')
        else:
            raise Exception('No drive')

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
baby = Baby()
adult = Adult()    



class Car(object):
    def __init__(self, model=None):
        self.model = model 
    def run(self):# これで model をインスタンス変数として保持
        print('run')
    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)



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