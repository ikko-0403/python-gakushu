class Person(object):

    kind = 'human'#self　を入れずに共通の変数、class変数として扱える。

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()

class T(object):
    
    def __init__(self):
        self.words = []

    def add_words(self, word):
         self.words.append(word)

c = T()
c.add_words('add 1')
c.add_words('add 2')
print(c.words)


d = T()
d.add_words('add 3')
d.add_words('add 4')

print(d.words)
