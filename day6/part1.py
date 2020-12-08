with open('./input.txt') as f:
  data = f.read().strip().split('\n\n')

p1 = map(lambda x: 
  reduce(lambda x,y: x.union(y), map(set, x.split('\n')))
, data)
print sum(map(len,p1))

p2 = map(lambda x: 
  reduce(lambda x,y: x.intersection(y), map(set, x.split('\n')))
, data)
print sum(map(len,p2))