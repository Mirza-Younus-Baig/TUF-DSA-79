class Solution:
    # declare as a global variable or a class variable
    def __init__(self):
        self.cnt = 0

    def mergeSort(self, arr, low, high):
        if low < high:
            mid = (low + high) // 2
            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid + 1, high)
            self.merge(arr, low, mid, high)


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
                # add all the no of elements from the left array
                self.cnt += mid - i + 1
            
        while i <= mid:
            res.append(arr[i])
            i += 1
        while j <= high:
            res.append(arr[j])
            j += 1
            
        for i in range(low, high + 1):
            arr[i] = res[i - low]


obj = Solution()
arr = [4,3,2,5,1,8,7,9,6]
obj.mergeSort(arr, 0, len(arr) - 1)
print("Number of inversion pairs:", obj.cnt)

