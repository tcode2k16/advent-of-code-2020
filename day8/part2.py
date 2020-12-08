with open('./input.txt') as f:
  data = f.read().strip().split('\n')

data = [
  [a, int(b)]
  for x in data
  for (a, b) in [x.split(' ')]
]
# print len(filter(lambda (x, _): x in ['nop', 'jmp'], data))


def test():
  visited = set()
  ip = 0
  acc = 0
  while ip not in visited and ip < len(data):
    instr, param = data[ip]
    visited.add(ip)
    if instr == 'nop':
      ip += 1
    elif instr == 'acc':
      acc += param
      ip += 1
    elif instr == 'jmp':
      ip += param
      
  return [ip == len(data), acc]

for i in range(len(data)):
  if data[i][0] == 'nop':
    data[i][0] = 'jmp'
    r, a = test()
    if r:
      print a
      break
    data[i][0] = 'nop'
  if data[i][0] == 'jmp':
    data[i][0] = 'nop'
    r, a = test()
    if r:
      print a
      break
    data[i][0] = 'jmp'

