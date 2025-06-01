class Solution:
    def findMin(self, arr):
        if len(arr) <= 1:
            return arr[0]
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l+r) // 2

            if arr[m] < arr[m-1]:
                return arr[m]
            if arr[m]  >= arr[r]:
                l = m + 1
            else:
                r = m
        
obj = Solution();
arr = [5,1,2,3,4]
res = obj.findMin(arr)

print(res)