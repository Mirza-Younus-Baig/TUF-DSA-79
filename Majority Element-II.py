class Solution:
    def majorityElement(self, nums):
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None

        for num in nums: 
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        for val in [candidate1, candidate2]:
            if nums.count(val) > len(nums) // 3:
                res.append(val)


        return res