with open('./input.txt') as f:
  data = f.read().strip().split('\n')

data = map(lambda x: x.replace('.','').replace('no other bags','').replace('bags','').replace('bag','').split(' contain '), data)
# data = map(lambda (a, b): [a, map(lambda x: (int(x[:x.index(' ')), x[x.index(' ')+1:]), b.split(', '))], data)
good = set()
d = {}
count = 0
while True:
  for line in data:
    name, content = line
    name = name.strip()
    content = map(lambda x: x.strip(), content.split(', '))
    content = map(lambda x: [
      int(x[:x.index(' ')]),
      x[x.index(' ')+1:]
    ] if len(x) > 1 else [], content)

    
    if name in d:
      continue

    if content == [[]]:
      d[name] = 0
      good.add(name)
      continue
    # print content
    # print zip(*content)
    nums, vals = zip(*content)
    vals = set(vals)
    
    if len(vals) == len(vals.intersection(good)):
      d[name] = sum(map(lambda (x,y): x*(d[y]+1), content))
      good.add(name)

    
    # if len(content) <= 0 or name in good:
    #   continue

    # nums, vals = content
    # vals = set(vals)
    # if len(good.intersection(vals)) > 0:
    #   good.add(name)
    #   count += 1
    # print name, content
  if 'shiny gold' in good:
    print d['shiny gold']