class Solution:
    def search(self, nums, k):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == k:
                return mid

            if nums[left] <= k < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
        return -1

obj = Solution()
arr = [4, 5, 6, 1, 2, 3]
k = 3
res = obj.search(arr, k)
print(res)

# class Solution:
#     def bsearch(self, nums,low, high, target) -> int:
#         left = low
#         right = high
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid + 1
#             elif nums[mid] > target:
#                 right = mid - 1
#         return -1


#     def search(self, nums, k):
#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             mid = (left + right) // 2
#             if nums[left] <= nums[mid]:
#                 ind = self.bsearch(nums, left, mid, k)
#                 if ind == -1:
#                     left = mid + 1
#                     continue
#                 else:
#                     return ind
#             else:
#                 ind = self.bsearch(nums, mid, right, k)
#                 if ind == -1:
#                     right = mid - 1
#                     continue
#                 else:
#                     return ind
#         return -1

