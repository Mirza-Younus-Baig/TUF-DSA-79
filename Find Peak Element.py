from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
        
        left = 1
        right = len(nums) - 2

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1]:
                left = mid + 1
            else:
                right = mid
        

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1],
        [3, 2, 1],
        [1, 2]
    ]

    for i, test in enumerate(test_cases):
        result = sol.findPeakElement(test)
        print(f"Test Case {i + 1}: Input = {test}, Peak Index = {result}, Peak Value = {test[result]}")