with open('./input.txt') as f:
  data = f.read().strip().split('\n')
  curr_t = int(data[0])
  ids = data[1].split(',')
  tmp = []
  for i in range(len(ids)):
    if ids[i] != 'x':
      tmp.append((i, int(ids[i])))
  ids = tmp
  # ids = map(int, filter(lambda x: x != 'x', data[1].split(',')))
print curr_t, ids

t = 0
inc = 1
while len(ids) > 0:
  off, val = ids.pop(0)
  while (t+off) % val != 0:
    t += inc
  inc *= val
  print t

# t = curr_t
# while True:
#   for each in ids:
#     if t % each == 0:
#       print (t-curr_t)*each
#       exit()
#   t += 1