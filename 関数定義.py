def say_something():
    s = "Hi"
    return s
result = say_something()
print(result)


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green papper'
    else:
        return "I don't KNOW"




result = what_is_this('green')
print(result)

result1 = what_is_this('red')
print(result1)

result2 = what_is_this('blue')
print(result2)