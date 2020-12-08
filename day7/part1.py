with open('./input.txt') as f:
  data = f.read().strip().split('\n')

data = map(lambda x: x.replace('.','').replace('no other bags','').replace('bags','').replace('bag','').split(' contain '), data)
# data = map(lambda (a, b): [a, map(lambda x: (int(x[:x.index(' ')), x[x.index(' ')+1:]), b.split(', '))], data)
good = set(['shiny gold'])
count = 0
while True:
  for line in data:
    name, content = line
    name = name.strip()
    content = map(lambda x: x.strip(), content.split(', '))
    content = zip(*map(lambda x: [
      int(x[:x.index(' ')]),
      x[x.index(' ')+1:]
    ] if len(x) > 1 else [], content))
    if len(content) <= 0 or name in good:
      continue

    nums, vals = content
    vals = set(vals)
    if len(good.intersection(vals)) > 0:
      good.add(name)
      count += 1
    # print name, content
  print count