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

s = 0
error_count = 0
for each in near:
  for e in each:
    for field, r in fields:
      if r[0] <= e <= r[1] or r[2] <= e <= r[3]:
        break
    else:
      error_count += 1
      s += e
      break


print len(near)
print error_count
print s