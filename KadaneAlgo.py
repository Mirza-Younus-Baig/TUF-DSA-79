class Solution:
    def maxSubArray(self, nums):
        currSum, maxSum = 0, float('-inf')
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(currSum, maxSum)
            if currSum < 0:
                currSum = 0
        return maxSum

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    result = Solution().maxSubArray(nums)
    print("Maximum Subarray Sum:", result)