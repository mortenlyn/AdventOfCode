import re

dicto = {1: [["N"], ["S"], ["D"], ["C"], ["V"], ["Q"], ["T"]], 
2: [["M"], ["F"], ["V"]], 
3: [["F"], ["Q"], ["W"], ["D"], ["P"], ["N"], ["H"], ["M"]],
4: [["D"], ["Q"], ["R"], ["T"], ["F"]],
5: [["R"], ["F"], ["M"], ["N"], ["Q"], ["H"], ["V"], ["B"]],
6: [["C"], ["F"], ["G"], ["N"], ["P"], ["W"], ["Q"]],
7: [["W"], ["F"], ["R"], ["L"], ["C"], ["T"]],
8: [["T"], ["Z"], ["N"], ["S"]],
9: [["M"], ["S"], ["D"], ["J"], ["R"], ["Q"], ["H"], ["N"]]}

def A():
  with open("input5.txt", "r") as f:
    info = [re.split(' |\n', x.strip()) for x in f.readlines()]

    for i in range(len(info)):
      dicto[int(info[i][-1])].extend((dicto[int(info[i][-3])])[-(int(info[i][1])):][::-1])
      del dicto[int(info[i][-3])][-(int(info[i][1])):]

    print(dicto)

# A()
# Anwer = FRDSQRRCD

def B():
  with open("input5.txt", "r") as f:
    info = [re.split(' |\n', x.strip()) for x in f.readlines()]

    for i in range(len(info)):
      dicto[int(info[i][-1])].extend((dicto[int(info[i][-3])])[-(int(info[i][1])):])
      del dicto[int(info[i][-3])][-(int(info[i][1])):]

    print(dicto)

B()

# Answer = HRFTQVWNN

  
  