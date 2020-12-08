import itertools

with open('./input.txt') as f:
  data = map(int, f.read().strip().split('\n'))


for (a,b,c) in itertools.combinations(data, 3):
  if a+b+c == 2020:
    print (a*b*c)
    exit()


