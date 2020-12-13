import math 

vals = ['.', 'L', '#']
with open('./input.txt') as f:
  data = f.read().strip().split('\n')
  row_s = len(data)
  col_s = len(data[0])

  data = [
    vals.index(v)
    for row in data
    for v in row.strip()
  ]
  
new_data = [0]*len(data)
l = len(data)
def mut(i):
  v = data[i]
  if v == 0:
    return v

  c = 0 # # of #
  notTop = i >= col_s
  notBottom = i < l - col_s
  notLeft = i % col_s != 0
  notRight = i%col_s != col_s - 1
  
  if notTop:
    c += 1 if data[i-col_s] == 2 else 0

  if notBottom:
    c += 1 if data[i+col_s] == 2 else 0

  if notLeft:
    c += 1 if data[i-1] == 2 else 0

  if notRight:
    c += 1 if data[i+1] == 2 else 0

  if notTop and notLeft:
    c += 1 if data[i-col_s-1] == 2 else 0

  if notTop and notRight:
    c += 1 if data[i-col_s+1] == 2 else 0

  if notBottom and notLeft:
    c += 1 if data[i+col_s-1] == 2 else 0

  if notBottom and notRight:
    c += 1 if data[i+col_s+1] == 2 else 0

  if v == 1 and c == 0:
    return 2

  if v == 2 and c >= 4:
    return 1

  return v

while True:
  count = 0
  for i in range(l):
    nv = mut(i)
    new_data[i] = nv
    if nv != data[i]:
      count += 1
  if count == 0:
    print data
    print len(filter(lambda x: x == 2, data))
    exit()
  print new_data
  data, new_data = new_data, data


print data