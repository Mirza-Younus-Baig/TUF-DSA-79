
# next_permutation : find next lexicographically greater permutation

# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

# Brute Force approach 

def perm(start, nums, result):
    if start == len(nums):
        result.append(nums[:])
        return
    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]  # swap
        perm(start + 1, nums, result)
        nums[start], nums[i] = nums[i], nums[start]  # backtrack


arr = list(map(int, input().split()))

nums = sorted(arr)
result = []
perm(0, nums, result)
result.sort()
print(result)
for i in range(len(result)):
    if result[i] == arr:
        if i + 1 != len(result):
            print(result[i+1])
            break
        else:
            print(result[0])



