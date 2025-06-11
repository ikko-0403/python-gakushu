#from practice.talk import human
#from practice.talk import animal
#from practice.talk import *


#print(animal.sing())
#print(animal.cry())


#print(human.sing())
#print(human.cry())

try:
    from practice import biile
except ImportError:
    from practice.tools import biile
print(biile.say_twice("seiko"))