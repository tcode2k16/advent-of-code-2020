with open('./input.txt') as f:
  data = f.read().strip().split('\n')
  # mask = data[0]
  # data = data[1:]
# print mask
# print data
include_mask = 0
val_mask = 0
mem = {}
for line in data:
  cmd, param = line.split(' = ')
  print cmd
  if 'mask' in cmd:
    include_mask = int(param.replace('1','0').replace('X', '1'),2)
    val_mask = int(param.replace('X', '0'), 2)
  if 'mem' in cmd:
    v = int(param)
    v = v & include_mask
    v = v | val_mask
    mem[int(cmd[4:-1])] = v
print sum(mem.values())