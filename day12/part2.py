with open('./input.txt') as f:
  data = f.read().strip().split('\n')
  data = [(line[0], int(line[1:])) for line in data]


ship_x = 0
ship_y = 0
point_x = 10
point_y = 1

def counter_rot(x, y):
  return (y, -x)

for (cmd, param) in data:
  if cmd == 'N':
    point_y += param
  if cmd == 'S':
    point_y -= param
  if cmd == 'E':
    point_x += param
  if cmd == 'W':
    point_x -= param
  if cmd == 'R':
    for i in range(param//90):
      point_x, point_y = counter_rot(point_x, point_y)
  if cmd == 'L':
    for i in range((param//90)*3):
      point_x, point_y = counter_rot(point_x, point_y)
  if cmd == 'F':
    ship_x += point_x * param
    ship_y += point_y * param
      

print ship_x, ship_y
print abs(ship_x) + abs(ship_y)
  

# print data
