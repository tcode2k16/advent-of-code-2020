with open('./input.txt') as f:
  data = f.read().strip().split('\n')


parse_field = lambda x: (x.split(': ')[0], [
  int(v)
  for e in x.split(': ')[-1].split(' or ')
  for v in e.split('-')
])
fields = map(parse_field, data[:data.index('')])

near = data[data.index('nearby tickets:')+1:]
near = [map(int, x.split(',')) for x in near]

ticket = map(int, data[data.index('your ticket:')+1].split(','))

s = 0
tmp = []
for each in near:
  for e in each:
    for field, r in fields:
      if r[0] <= e <= r[1] or r[2] <= e <= r[3]:
        break
    else:
      s += e
      break
  else:
    tmp.append(each)


print len(near)
print s
near = tmp

l = []
print l
# print near
# print 

for col in zip(*near):
  # print col
  tmp = []
  for field, r in fields:
    for e in col:
      if not (r[0] <= e <= r[1] or r[2] <= e <= r[3]):
        break
    else:
      tmp.append(field)
  l.append(tmp)
print map(len, l)
print l


found = set()
# print filter(lambda x: len(x) == 1 and x[0] not in found, l)
while len(found) != len(l):
  for each in filter(lambda x: len(x) == 1 and x[0] not in found, l):
    each = each[0]
    found.add(each)
    for possible_vals in l:
      if each in possible_vals and len(possible_vals) > 1:
        possible_vals.remove(each)
l = map(lambda x: x[0], l)
p = 1
for i in range(len(l)):
  each = l[i]
  if 'departure' in each:
    p *= ticket[i]
print p
# print l
