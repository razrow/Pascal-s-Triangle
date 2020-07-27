#Given numRows, generate the first numRows of Pascal’s triangle.

#Pascal’s triangle : To generate a given row in Pascal's Triangle (we'll call it R):
#for R[i] in row R, sum up R[i] and R[i-1] from previous row R - 1.
def pascal_triangle(numRows):
  i = 1
  R = [1]
  list = []
  while i <= numRows:
    if i == 1:
      print(R)
      list.append(R.copy())
    val = 0
    placeholder = 1
    if i == 2:
      R.append(1)
      print(R)
      list.append(R.copy())
    if i > 2:
      R2 = []
      R3 = [1]
      for a in range (0, len(R)):
        R2.append(R[a])
      for j in range (0,len(R)-1):
        for k in range (j+1,len(R)):
          val = R[j] + R2[k]
          R3.append(val)
          placeholder = placeholder + 1
          break
      R3.append(1)
      R.clear()
      R = R3.copy()
#      for x in range (0, len(R3)):
#        R.append(R3[x])
      print(R)
      list.append(R3.copy())
    i = i+1
  return list
  pass

pascal_triangle(5)