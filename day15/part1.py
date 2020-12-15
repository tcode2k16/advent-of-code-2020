# data = '0,3,6'
data = '2,15,0,9,1,20'
data = map(int, data.split(','))
d = {}
p = -1
t = 0
for v in data:
  d[v] = t
  p = v
  t += 1

n = 0
for _ in range(30000000-len(data)-1):
  # print n
  if n in d:
    tmp = t - d[n]
  else:
    tmp = 0
  d[n] = t
  n = tmp
  t += 1

print n

# print d