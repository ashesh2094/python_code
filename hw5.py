# Create Target Array in the Given Order


def Target(nums, index):
    if len(nums) == 0:
        return []
    target = [nums[0]]
    for i in range(1, len(nums)):
        target[index[i]:index[i]] = [nums[i]]
    return target


a = Target([0,1,2,3,4], [0,1,2,2,1])
print(a)