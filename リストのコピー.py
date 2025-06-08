
i = [1,2,3,4,5,6]
j = i
j[0] = 100

print("j =",i)
print("i =",j)

x = [1,2,3,4,5,]
y = x.copy()
# y = x[:]
y[0] = 100

print("y =",y)
print("y =",x)