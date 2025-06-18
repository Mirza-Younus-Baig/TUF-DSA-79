# Brute force approach


def maxAreaRectangle(arr):
    maxArea = 0
    n = len(arr)
    for i in range(n):
        minHeight = 99999
        for j in range(i, n):
            minHeight = min(minHeight, arr[j])
            maxArea = max(maxArea, minHeight * (j - i + 1))
    
    return maxArea

if __name__ == "__main__":
    arr = [2,1,5,6,2,3]
    print(maxAreaRectangle(arr))
