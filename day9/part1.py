from collections import deque

with open('./input.txt') as f:
  data = map(int, f.read().strip().split('\n'))

def part1():
  tracking_len = 25
  tracking = deque(data[:tracking_len])
  for each in data[tracking_len:]:
    for c in tracking:
      if each - c in tracking:
        break
    else:
      print each
      return each
    tracking.popleft()
    tracking.append(each)

    
def part2():
  target = part1()

  
  tracking = deque()
  s = sum(tracking)
  i = 0

  while True:
    while s < target and i < len(data):
      s += data[i]
      tracking.append(data[i])
      i += 1
    if s == target:
      return max(tracking)+min(tracking)
    s -= tracking.popleft()

  

    
print part2()