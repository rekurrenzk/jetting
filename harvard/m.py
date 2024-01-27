def getAverage():
  l1 = [1, 4, 9, 10, 23]
  lenl1 = len(l1)
  nums_total = 0
  for nums in l1:
      nums_total += nums
      
  avg = nums_total / lenl1
  return avg

av = getAverage()
print(av)



print("--------------------------")
"""
or this could be in another way
"""
print("--------------------------")


def getAverage():
    l1 = [1, 4, 9, 10, 23]
    avg = sum(l1) / len(l1)
    return avg

av = getAverage()
print(av)


print("--------------------------")



def removeList():
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]
    l1 = [x for x in l1 if x not in l2]
    return l1
rl = removeList()
print(rl)

print("--------------------------")
"""
or this could be in another way
"""
print("--------------------------")

def removeList():
    l1 = [1, 4, 9, 10, 23]
    l2 = [4, 9]
    
    for elem in l2:
        if elem in l1:
            l1.remove(elem)
        return l1

l1 = removeList()
print(l1)