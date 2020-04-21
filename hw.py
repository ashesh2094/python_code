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


