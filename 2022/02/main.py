with open("input2.txt", "r") as f:
  matchhand = f.read().strip().split("\n")
  eachhand = [x.split() for x in matchhand]

def A(): 
  points = []
  for i in range(len(eachhand)):
    
    if eachhand[i][0] == "A":
      if eachhand[i][1] == "X":
        points.append(4)
      elif eachhand[i][1] == "Y":
        points.append(8)
      else:
        points.append(3)
    elif eachhand[i][0] == "B":
      if eachhand[i][1] == "X":
        points.append(1)
      elif eachhand[i][1] == "Y":
        points.append(5)
      else:
        points.append(9)
    elif eachhand[i][0] == "C":
      if eachhand[i][1] == "X":
        points.append(7)
      elif eachhand[i][1] == "Y":
        points.append(2)
      else:
        points.append(6)
    
  print(sum(points))

A()

def B():

  points = []

  for i in range(len(eachhand)):
    
    if eachhand[i][1] == "X":
      if eachhand[i][0] == "A":
        points.append(3)
      elif eachhand[i][0] == "B":
        points.append(1)
      else:
        points.append(2)
    elif eachhand[i][1] == "Y":
      if eachhand[i][0] == "A":
        points.append(4)
      elif eachhand[i][0] == "B":
        points.append(5)
      else:
        points.append(6)
    elif eachhand[i][1] == "Z":
      if eachhand[i][0] == "A":
        points.append(8)
      elif eachhand[i][0] == "B":
        points.append(9)
      else:
        points.append(7)
  
  print(sum(points))

B()