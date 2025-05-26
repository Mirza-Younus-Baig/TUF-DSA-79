

from typing import List

class Solution:
    def perm(self, start, res, nums):
        if start == len(nums):
            res.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]
            self.perm(start + 1, res, nums)
            nums[i], nums[start] = nums[start], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.perm(0, res, nums)
        return res

if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 2, 3]
    print(f"Permutations of {nums1}:")
    print(sol.permute(nums1))

    # Test case 2
    nums2 = [0, 1]
    print(f"\nPermutations of {nums2}:")
    print(sol.permute(nums2))

    # Test case 3
    nums3 = [1,6,2,4]
    print(f"\nPermutations of {nums3}:")
    print(sol.permute(nums3))