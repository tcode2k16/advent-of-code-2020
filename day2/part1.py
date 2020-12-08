with open('./input.txt') as f:
  data = f.read().strip().split('\n')


count = 0
for line in data:
  requirement, password = line.split(': ')
  range_, letter = requirement.split(' ')
  low, high = map(int, range_.split('-'))
  if low <= password.count(letter) <= high:
    count += 1

print count