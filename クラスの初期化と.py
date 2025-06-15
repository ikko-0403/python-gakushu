class Person(object):#この人が         (コンストラクタ)
    def __init__(self, name):#関数自身の引数保持される
        self.name = name
        print(self.name)


    def say_something(self):#何か言う
        print('I am {}, Hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)
        
    def __del__(self):
        print('Good Bye')



person = Person('Ikko')
person.say_something()