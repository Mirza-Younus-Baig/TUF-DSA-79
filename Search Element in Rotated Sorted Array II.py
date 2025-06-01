class Solution:
    def search(self, nums, k):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == k:
                return mid

            # If duplicates make it hard to decide
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= k < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < k <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

obj = Solution()
# arr = [2,5,6,0,0,1,2]
arr = [1,1,0,1,1]
k = 0
res = obj.search(arr, k)
print(res)