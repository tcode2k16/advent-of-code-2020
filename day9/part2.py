from collections import deque

with open('./sample-input.txt') as f:
  data = map(int, f.read().strip().split('\n'))

tracking_len = 25
tracking = deque(data[:tracking_len])
s = sum(tracking)
target = 
for each in data[tracking_len:]:
  for c in tracking:
    if each - c in tracking:
      break
  else:
    print each
    exit()
  tracking.popleft()
  tracking.append(each)

  
print data