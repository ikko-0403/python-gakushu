

def say_something(word, *args):#タプルに入れてくれる
    print('word =', word)#wordのとこだけ引数渡して、、残りはargsに入る
    for arg in args:
        print(arg)

say_something('Hi', 'Mike', 'Hou are you?')