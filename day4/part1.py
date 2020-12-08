
with open('./input.txt') as f:
  data = f.read().strip().split('\n\n')

count = 0
for each in data:
  pairs = map(lambda x: x.split(':'), each.replace(' ','\n').split('\n'))
  d = {}
  for [k, v] in pairs:
    d[k] = v
  print d.keys()



  for k in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
    if k not in d:
      break
  else:
    count += 1
print count
