def A():
  with open("input6.txt", "r") as f:
    string = "".join([x for x in f])

    for i, j in enumerate(string[:-1]):
      l = sorted(list(string[i:i+4]))
      s = set(l)
      s = sorted(list(s))

      if s == l:
        return i+4

print(A())
    
def B():
  with open("input6.txt", "r") as f:
    string = "".join([x for x in f])

    for i, j in enumerate(string[:-1]):
      l = sorted(list(string[i:i+14]))
      s = set(l)
      s = sorted(list(s))

      if s == l:
        return i+14   

print(B())



  
    