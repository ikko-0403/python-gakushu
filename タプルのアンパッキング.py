#タプルのアンパッキング「

t = 0,100
x, y = t
print(type(t))
print(x, y)

tmp = x
x = y
y = tmp
print(x, y)

a = 1
b = 5
print(a, b)
a, b = b, a
print(a, b)