import sys
sys.setrecursionlimit(1500)

with open('./input.txt') as f:
  data = map(int, f.read().strip().split('\n'))


data = sorted(data)
print data

d = [0]*(len(data)+1)

def prop(v, i):
  print '{}: {}'.format(v, i)
  if d[i] != 0:
    return d[i]
    
  if i == len(data):
    d[i] = 1
    return 1

  s = 0
  t = i
  while t < len(data) and data[t] <= v+3:
    s += prop(data[t], t+1)
    t += 1
  
  d[i] = s
  return s

print prop(0, 0)
print data
print d
# print '\n'.join([ '{:10} : {:10}'.format(data[i], d[i]) for i in range(len(data)) ])
# diff = [0]*4
# last = 0
# for each in data:
#   diff[each-last] += 1
#   last = each
# diff[3] += 1
# print diff
# print diff[1] * diff[3]