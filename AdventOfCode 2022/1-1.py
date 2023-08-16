with open("input.txt", "r") as f:
  calories = f.read().strip().split("\n\n")
  new = []

  for i in range(len(calories)):
    new.append(calories[i].split())

  intlist = []

  for i in range(len(new)):
    intlist.append([int(j) for j in new[i]])

  sumlist = []

  for i in range(len(intlist)):
    sumlist.append((sum(intlist[i])))


  sumlist = sorted(sumlist)  
  # Mest kalorier
  mostcal = sumlist[-1]
  # Summen av de tre med mest kalorier
  threelast = (sumlist[-3:])

  print(mostcal, threelast, sum(threelast))

  
  

  
  
  
   
