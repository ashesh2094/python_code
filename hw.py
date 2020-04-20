print("Decompress Run-Length Encoded List")

# input = [1,2,3,4]
# output = [2,4,4,4]

def findNum(num):
  output = []
  i = 0
  while i < len(num):
    for j in range(num[i]):
      output.append(i+2)
    i += 2
  return output
  
a=find([1,2,3,4])
print(a)



print("-----------------------------------------------------------------------------------------------------------------------")

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

print("------------------------------------------------------------------------------------------------------------------------")


