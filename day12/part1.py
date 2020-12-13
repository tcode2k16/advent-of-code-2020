with open('./input.txt') as f:
  data = f.read().strip().split('\n')
  data = [(line[0], int(line[1:])) for line in data]


curr_d = 0
x = 0
y = 0
for (cmd, param) in data:
  if cmd == 'N':
    y += param
  if cmd == 'S':
    y -= param
  if cmd == 'E':
    x += param
  if cmd == 'W':
    x -= param
  if cmd == 'R':
    curr_d = (curr_d + param) % 360
  if cmd == 'L':
    curr_d = (curr_d - param) % 360
  if cmd == 'F':
    if curr_d == 0:
      x += param
    elif curr_d == 90:
      y -= param
    elif curr_d == 180:
      x -= param
    elif curr_d == 270:
      y += param
      
    print curr_d
print x, y
print abs(x) + abs(y)
  

# print data
