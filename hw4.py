#  Find Numbers with Even Number of Digits

def findNumbers(nums):
    even = 0
    for i in nums:
        count = 0
        while i:
            i //= 10
            count += 1
        if count % 2 == 0:
            even += 1
    return even


a= findNumbers([12,345,2,6,7896])
print(a)
