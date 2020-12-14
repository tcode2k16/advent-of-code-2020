import itertools
with open('./input.txt') as f:
  data = f.read().strip().split('\n')
  # mask = data[0]
  # data = data[1:]
# print mask
# print data
float_mask = 0
val_mask = 0
floats = []
mem = {}
for line in data:
  cmd, param = line.split(' = ')
  print cmd
  if 'mask' in cmd:
    float_mask = int(param.replace('1','0').replace('X', '1'),2)
    val_mask = int(param.replace('X', '0'), 2)

    tmp = float_mask
    f = 1
    floats = []
    while tmp > 0:
      if tmp & 1:
        floats.append(f)
      tmp >>= 1
      f <<= 1
    floats = zip(floats, [0]*len(floats))
    print floats
  if 'mem' in cmd:
    addr = int(cmd[4:-1])
    v = int(param)
    addr = (addr & (~float_mask)) | val_mask
    for each in itertools.product(*floats):
      print bin(addr+sum(each))
      mem[addr+sum(each)] = v
print mem
print sum(mem.values())