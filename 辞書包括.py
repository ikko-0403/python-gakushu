w = ['mon', 'tue', 'wed', 'thu', 'fri', 'sun']
f = ['coffee', 'milk', 'water']

d  = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w,f)}

print(d)