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
  s_up = i//col_s
  s_down = (l-i-1)//col_s
  s_left = i%col_s
  s_right = (col_s-1)-(i%col_s)

  for j in range(1, s_up+1):
    t = i-col_s*j
    if data[t] != 0:
      c += 1 if data[t] == 2 else 0
      break
  
  for j in range(1, s_down+1):
    t = i+col_s*j
    if data[t] != 0:
      c += 1 if data[t] == 2 else 0
      break

  
  for j in range(1, s_left+1):
    t = i-j
    if data[t] != 0:
      c += 1 if data[t] == 2 else 0
      break

  
  for j in range(1, s_right+1):
    t = i+j
    if data[t] != 0:
      c += 1 if data[t] == 2 else 0
      break

  
  for j in range(1, min(s_up, s_left)+1):
    t = i+(-col_s-1)*j
    if data[t] != 0:
      c += 1 if data[t] == 2 else 0
      break

  
  for j in range(1, min(s_up, s_right)+1):
    t = i+(-col_s+1)*j
    if data[t] != 0:
      c += 1 if data[t] == 2 else 0
      break

  
  for j in range(1, min(s_down, s_left)+1):
    t = i+(col_s-1)*j
    if data[t] != 0:
      c += 1 if data[t] == 2 else 0
      break

  
  for j in range(1, min(s_down, s_right)+1):
    t = i+(col_s+1)*j
    if data[t] != 0:
      c += 1 if data[t] == 2 else 0
      break

  # print c
  if v == 1 and c == 0:
    return 2

  if v == 2 and c >= 5:
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