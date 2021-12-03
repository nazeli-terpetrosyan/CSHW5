def saveMatrixToFile(path, m):
  file = open(path, "w")
  for i in range(len(m)):
    for j in range(len(m[0])):
      file.write(str(m[i][j]) + ",")
    file.write("\n")
  file.close()
  pass

def loadMatrixFromFile(path):
  file = open(path)
  lines = file.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    lines[i] = lines[i][:-1]
    for j in range(len(lines[i])):
      lines[i][j] = int(lines[i][j])
  return lines