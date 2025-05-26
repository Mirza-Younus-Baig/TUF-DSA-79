
# next_permutation : find next lexicographically greater permutation

# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

# Brute Force approach 

# arr = list(map(int, input().split()))
# arr = [5,1,4,3,2]
# arr = [5,1,2,3,2]
# arr = [3,2,1]
# arr = [1, 3, 2] 
arr = [2,2,7,5,4,3,2,2,1]

# To run brute force approach

# def perm(start, nums, result):
#     if start == len(nums):
#         result.append(nums[:])
#         return
#     for i in range(start, len(nums)):
#         nums[start], nums[i] = nums[i], nums[start]  # swap
#         perm(start + 1, nums, result)
#         nums[start], nums[i] = nums[i], nums[start]  # backtrack

# nums = sorted(arr)
# result = []
# perm(0, nums, result)
# result.sort()
# print(result)
# for i in range(len(result)):
#     if result[i] == arr:
#         if i + 1 != len(result):
#             print(result[i+1])
#             break
#         else:
#             print(result[0])



# To run optimal approach
ind = 0
for i in range(len(arr) - 1, 0, -1):
    if arr[i-1] < arr[i]:
        ind = i
        break
else:
    arr.reverse()
    print(arr)
    # Don't exit here; let the program end naturally

next_greater = float('inf')
maxInd = ind
for i in range(ind, len(arr)):
    if arr[i] > arr[ind - 1] and arr[i] < next_greater:
        next_greater = arr[i]
        maxInd = i
arr[ind - 1], arr[maxInd] = arr[maxInd], arr[ind - 1]

# Correctly sort the suffix in-place
arr[ind:] = sorted(arr[ind:])

print(arr)




