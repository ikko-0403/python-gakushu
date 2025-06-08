animal = 'cat'

def f():
    #print(animal)
    animal = 'dog'
    print('after', animal)

f()
print('global:', animal)

ani = 'cat'

def f():
    ani = 'dog'
    print('local:', locals())#関数内の変数￥を辞書型で返す関数

f()
print('global:', ani)