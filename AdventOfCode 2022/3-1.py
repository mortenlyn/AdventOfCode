import string
def A():
  with open("input3.txt", "r") as f:
    compartements = [x.strip().split('\n') for x in f.readlines()]

    priorities = []
    for i in range(len(compartements)):
      comp = list(compartements[i][0])

      middle_index = len(comp)//2

      firstcomp = set(comp[0:middle_index])
      secondcomp = set(comp[middle_index:])

      priorities.append(firstcomp.intersection(secondcomp))


  low_letter = list(string.ascii_lowercase)
  upper_letter = list(string.ascii_uppercase)

  res = list(map(''.join, priorities))

  score = []
  for i in range(len(res)):
    if res[i] in low_letter:
      score.append(low_letter.index(res[i])+1)
      
    elif res[i] in upper_letter:
      score.append((upper_letter.index(res[i]))+27)
    else:
    
      print(res[i])

  print(sum(score))



def B():
  with open("input3.txt", "r") as f:
    compartements = [x.strip().split('\n') for x in f.readlines()]

    priorities = []
    for i in range(0, len(compartements), 3):
      new = (compartements[i:i + 3])
     
      set1 = set(new[0][0])
      set2 = set(new[1][0])
      set3 = set(new[2][0])

      interelem = (list((set1).intersection(set2)))
      interelemfinal = (list((set(interelem)).intersection(set3)))
      
      priorities.append(interelemfinal[0])

    low_letter = list(string.ascii_lowercase)
    upper_letter = list(string.ascii_uppercase)     
    
    score = []
    for i in range(len(priorities)):
      if priorities[i] in low_letter:
        score.append(low_letter.index(priorities[i])+1)
        
      elif priorities[i] in upper_letter:
        score.append((upper_letter.index(priorities[i]))+27)
      else:
      
        print(priorities[i])

    print(sum(score))


B()
  



    



  



    

