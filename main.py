def eca(cells, rule):
  result = []
  cellslen = len(cells)
  c = "0" + cells + "0"
  rulebits = '{0:08b}'.format(rule)
  neighbourstonext = {'{0:03b}'.format(n):rulebits[::-1][n] for n in range(8)}
  result.append(c[1:-1])
  print(result)
  while True:
    for x in range(0,lines):
      c = ''.join(['0',''.join(neighbourstonext[c[i-1:i+2]] for i in range(1, cellslen + 1)),'0'])
      result.append(c[1:-1])
      print(result)
    return result
 
if __name__ == '__main__':
    lines = 15
    base = '0000000000000001000000000000000'
    rule = 109
    zipped = [range(lines + 1)] + [eca(base, rule)]
    for data in zip(*zipped):
      i = data[0]
      cells = data[1:]
      print('%s' % (''.join(cells).replace('0', '  ').replace('1', '██')))