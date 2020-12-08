with open('./input.txt') as f:
  data = f.read().strip().split('\n')


count = 0
for line in data:
  tmp = 0
  requirement, password = line.split(': ')
  range_, letter = requirement.split(' ')
  low, high = map(int, range_.split('-'))
  if low-1 < len(password) and  password[low-1] == letter:
    tmp += 1
  if high-1 < len(password) and password[high-1] == letter:
    tmp += 1
  if tmp == 1:
    count += 1
  

print count