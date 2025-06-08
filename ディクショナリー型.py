
d = {"X": 100, "Y": 200}
print(d.keys())

d2 = {"X": 300, "z": 1010101010}

d.update(d2)
print(d)

d.pop("X")
print(d)

print("X" in d)
print("Y" in d)