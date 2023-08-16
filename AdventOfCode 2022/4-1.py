import re

def A():
  with open("input4.txt ", "r") as f:
    lines = [re.split(',|-', x.strip()) for x in f.readlines()]
    
    nums = [list(map(int, row)) for row in lines]
  
    pairs = 0
    for i in range(len(nums)):
      
      if (nums[i][0] >= nums[i][-2]) and (nums[i][1] <= nums[i][-1]):
        pairs += 1
        
      elif (nums[i][-2] >= nums[i][0]) and (nums[i][-1] <= nums[i][1]):
        pairs += 1
      else:
        print(lines[i])
        pass
    
    print(pairs)

# A()

def B():
  with open("input4.txt ", "r") as f:
    lines = [re.split(',|-', x.strip()) for x in f.readlines()]
    
    nums = [list(map(int, row)) for row in lines]
  
    pairs = 0
    for i in range(len(nums)):
      
      if (nums[i][0] >= nums[i][-2] and nums[i][0] <= nums[i][-1]) or (nums[i][1] <= nums[i][-1] and nums[i][1] >= nums[i][-2]):
        pairs += 1
        
      elif (nums[i][-1] >= nums[i][0] and nums[i][-1] <= nums[i][1]) or (nums[i][-2] <= nums[i][1] and nums[i][-2] >= nums[i][0]):
        pairs += 1
      else:
        # print(lines[i])
        pass
  
    print(pairs)

B()