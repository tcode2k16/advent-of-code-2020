with open('./input.txt') as f:
  data = f.read().strip().split('\n')

data = [
  [a, int(b)]
  for x in data
  for (a, b) in [x.split(' ')]
]
# print len(filter(lambda (x, _): x in ['nop', 'jmp'], data))

visited = set()
ip = 0
acc = 0
while ip not in visited:
  instr, param = data[ip]
  visited.add(ip)
  if instr == 'nop':
    ip += 1
  elif instr == 'acc':
    acc += param
    ip += 1
  elif instr == 'jmp':
    ip += param
    
print acc