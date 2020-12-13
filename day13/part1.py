with open('./input.txt') as f:
  data = f.read().strip().split('\n')
  curr_t = int(data[0])
  ids = map(int, filter(lambda x: x != 'x', data[1].split(',')))
print curr_t, ids

t = curr_t
while True:
  for each in ids:
    if t % each == 0:
      print (t-curr_t)*each
      exit()
  t += 1
