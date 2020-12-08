
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
    try:
      if len(d['byr']) == 4 and 1920 <= int(d['byr']) <= 2002 and \
         len(d['iyr']) == 4 and 2010 <= int(d['iyr']) <= 2020 and \
         len(d['eyr']) == 4 and 2020 <= int(d['eyr']) <= 2030 and \
         ((d['hgt'][-2:] == 'cm' and 150 <= int(d['hgt'][:-2]) <= 193) or (d['hgt'][-2:] == 'in' and 59 <= int(d['hgt'][:-2]) <= 76)) and \
         len(d['hcl']) == 7 and d['hcl'][0] == '#' and int(d['hcl'][1:], 16) >= 0 and \
         d['ecl'] in 'amb blu brn gry grn hzl oth'.split(' ') and \
         len(d['pid']) == 9 and int(d['pid']) >=0:
        count += 1
    except:
      pass
print count

