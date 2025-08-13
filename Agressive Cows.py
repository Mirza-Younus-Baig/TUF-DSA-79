class Solution:
    def canWePlace(self, nums, mid, k):
        cnt = 1
        last = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - last >= mid:
                  last = nums[i]
                  cnt += 1
            if cnt >= k:
                return True
        return False
             
      
    def aggressiveCows(self, nums, k):
        nums.sort()
        low = 1
        high = nums[-1] - nums[0]
        res = -1
        while low <= high:
            mid = (low + high) // 2
            if self.canWePlace(nums, mid, k):
                res = mid
                low = mid + 1
            else:
                 high = mid - 1
        return high