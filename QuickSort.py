class Solution:
    def partition(self, nums, low, high):
        i = low - 1
        j = high + 1
        pivot = nums[low]

        while True:
            i += 1
            while pivot > nums[i]:
                i += 1
            j -= 1
            while pivot < nums[j]:
                j -= 1
            
            if i >= j:
                return j
            
            nums[i], nums[j] = nums[j], nums[i]

    def quicksort(self, nums, low, high):
        if low < high:
            j = self.partition(nums, low, high)
            self.quicksort(nums, low, j)
            self.quicksort(nums, j + 1, high)

obj = Solution()
nums = [3,8,1,2,3,4,1,5]
print("Before sorting", nums)
obj.quicksort(nums, 0, len(nums) - 1)
print("After sorting", nums)