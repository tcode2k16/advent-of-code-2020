with open('./input.txt') as f:
  data = f.read().strip().split('\n')


data = map(lambda x: (
  int(x[:7].replace('F','0').replace('B', '1'), 2),
  int(x[7:].replace('L','0').replace('R', '1'), 2)
), data)
data = map(lambda (a,b): a*8+b, data)
print max(data)
s = set(range(8, 128*8-8))
for each in data:
  s.remove(each)
print s
