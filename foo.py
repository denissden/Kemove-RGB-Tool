import json



map = []


end = 695 / 800
c = 13
for x in range(c):
    map.append((end * x / c, 0, end * (x + 1) / c, 0.2))
map.append((0.86875, 0, 1, 0.2))  # BACKSPACE

print(map)

inc = 0.1
end = 720 / 800 - inc
c = 12
map.append((0, 0.2, inc, 0.4))  # TAB
for x in range(c):
    map.append((end * x / c + inc, 0.2, end * (x + 1) / c + inc, 0.4))
map.append((0.9019230769230769, 0.2, 1, 0.4))  # BACKSLASH

print(map)

inc = 0.11875
end = 680 / 800 - inc
c = 11
map.append((0, 0.4, inc, 0.6))  # CAPS
for x in range(c):
    map.append((end * x / c + inc, 0.4, end * (x + 1) / c + inc, 0.6))
map.append((0.85, 0.4, 1, 0.6))  # ENTER

print(map)

inc = 0.15
end = 655 / 800 - inc
c = 10
map.append((0, 0.6, inc, 0.8))  # LSHIFT
for x in range(c):
    map.append((end * x / c + inc, 0.6, end * (x + 1) / c + inc, 0.8))
map.append((0.81875, 0.6, 1, 0.8))  # RSHIFT

print(map)

inc = 0
end = 200 / 800 - inc
c = 3
for x in range(c):
    map.append((end * x / c + inc, 0.8, end * (x + 1) / c + inc, 1))
map.append((0.25, 0.8, 535 / 800, 1))  # SPACE

inc = 535 / 800
end = 735 / 800 - inc
c = 3
for x in range(c):
    map.append((end * x / c + inc, 0.8, end * (x + 1) / c + inc, 1))

map.append((735 / 800, 0.8, 1, 1))



input()
with open("map61key.json", "w+") as f:
    json.dump(map, f, )