
#集合型
#ディクショナリーと違って　{"x": }がないのでsetになる

a = {1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4}
b = {1,3,9}

print(type(a))
print(a)
print(a - b)
print(b - a)
print(a & b)
print(a | b)
print(a ^ b)