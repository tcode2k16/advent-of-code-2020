with open('./input.txt') as f:
  data = map(int, f.read().strip().split('\n'))


data = sorted(data)
diff = [0]*4
last = 0
for each in data:
  diff[each-last] += 1
  last = each
diff[3] += 1
print diff
print diff[1] * diff[3]