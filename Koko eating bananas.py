from math import ceil

class Solution:
    def minimumRateToEatBananas(self, nums, h):
        # Binary search to find the minimum eating speed such that
        # Koko can eat all bananas within h hours
        left = 1
        right = max(nums)
        result = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            for pile in nums:
                hours += ceil(pile / mid)

            if hours > h:
                left = mid + 1
            else:
                result = mid
                right = mid - 1

        return result

obj = Solution()
nums = [7, 15, 6, 3]
h = 8
print(obj.minimumRateToEatBananas(nums, h))

assert(obj.minimumRateToEatBananas([7, 15, 6, 3], 8) == 5)
assert(obj.minimumRateToEatBananas([25, 12, 8, 14, 19], 5) == 25)