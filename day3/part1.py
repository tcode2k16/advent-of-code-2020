with open('./input.txt') as f:
  data = f.read().strip().split('\n')


def do_slope(s):
  a,b = s
  count = 0
  col_idx = 0
  for i in range(0, len(data), b):
    line = data[i]
    if line[col_idx] == '#':
      count += 1
    col_idx = (col_idx+a)%len(line)
  return count

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

ans = 1
for each in map(do_slope, slopes):
  ans *= each
print ans
# print count