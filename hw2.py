print("Two Sum")

# input = [2,7,6,8]
# target = 9
# output = [0,1]

def TwoSum(num, target):

  for i in range (len(num)):
    for j in range(i+1,len(num)):
      sum = num[i] + num[j]
      if sum == target:
        return [i,j]

a = TwoSum([2,7,6,8],9)
print(a)
