class Solution:
    # declare as a global variable or a class variable
    def __init__(self):
        self.cnt = 0

    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.cnt
    
    def mergeSort(self, arr, low, high):
        if low < high:
            mid = (low + high) // 2
            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid + 1, high)
            self.countReverse(arr, low, mid, high)
            self.merge(arr, low, mid, high)

    def countReverse(self, arr, low, mid, high):
        j = mid + 1
        for i in range(low, mid + 1):
            while j <= high and arr[i] > 2 * arr[j]:
                j += 1
            self.cnt += j - mid - 1
    

    def merge(self, arr, low, mid, high):
        res = []
        i = low
        j = mid + 1

        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else:
                res.append(arr[j])
                j += 1
            
        while i <= mid:
            res.append(arr[i])
            i += 1
        while j <= high:
            res.append(arr[j])
            j += 1
            
        for i in range(low, high + 1):
            arr[i] = res[i - low]


obj = Solution()
arr = [1,3,2,3,1]
obj.mergeSort(arr, 0, len(arr) - 1)
print("Number of inversion pairs:", obj.cnt)

