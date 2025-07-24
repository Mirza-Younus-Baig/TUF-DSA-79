# Mathematical Approach
# Can also be solved using XOR

class Solution:
    def findErrorNums(self, nums):
        total, realTotal = 0, 0
        totalSquare, realTotalSquare = 0, 0
        n = len(nums)
        realTotal = (n * (n + 1))//2
        realTotalSquare = (n * (n + 1) * (2*n + 1))//6

        for i in nums:
            total += i
            totalSquare += i * i
        x = realTotal - total # A - B
        y = realTotalSquare - totalSquare # A2- B2
        y = y // x # A + B

        A, B = 0, 0
        A = (x + y) // 2
        B = y - A
        return [B, A]
