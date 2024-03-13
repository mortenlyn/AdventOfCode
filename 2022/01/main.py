with open("input.txt", "r") as f:
  calories = f.read().strip().split("\n\n")
  new = [calories[i].split() for i in range(len(calories))]
  intlist = [[int(j) for j in item] for item in new]
  sumlist = [sum(item_) for item_ in intlist]
  sumlist = sorted(sumlist)
  # Mest kalorier
  mostcal = sumlist[-1]
  # Summen av de tre med mest kalorier
  threelast = (sumlist[-3:])

  print(mostcal, threelast, sum(threelast))

  
  

  
  
  
   
