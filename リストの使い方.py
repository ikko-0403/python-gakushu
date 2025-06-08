seat = []
min = 0
max = 2

seat.append("p")

print(min <= len(seat) < max)

seat.append("p")

print(min <= len(seat) < max)

seat.pop(0)

print(min <= len(seat) < max)
