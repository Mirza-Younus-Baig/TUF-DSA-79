# Contents: 
# 1. Brute force approach
# 2. Better Solution
# 3. Optimal Solution

# 1. Brute Force approach
def maxAreaRectangle1(arr):
    maxArea = 0
    n = len(arr)
    for i in range(n):
        minHeight = 99999
        for j in range(i, n):
            minHeight = min(minHeight, arr[j])
            maxArea = max(maxArea, minHeight * (j - i + 1))
    
    return maxArea


# 2. Better Solution
def maxAreaRectangle2(arr):
    nle = []
    ple = []
    st = []
    n = len(arr)
    # to find next least element (from left to right)
    for i in range(n - 1, -1, -1):
        while st and arr[i] <= arr[st[-1]]:
            st.pop()
        if not st:
            nle.append(n-1)
        else:
            nle.append(st[-1] - 1)
        st.append(i)
    nle = nle[::-1] 
    
    # clear the stack to reuse it
    while st:
        st.pop()
    
    # to find previous least element (from right to left)
    for i in range(n):
        while st and arr[i] >= arr[st[-1]]:
            st.pop()
        
        if not st:
            ple.append(0)
        else:
            ple.append(st[-1] + 1)
        st.append(i)
    ple = ple[::-1]

    maxArea = 0
    for i in range(n):
        maxArea = max(maxArea, (ple[i] - nle[i] + 1) * arr[i])

    return maxArea

if __name__ == "__main__":
    arr = [2,1,5,6,2,3]
    print("Brute Force: " , maxAreaRectangle1(arr))

    print("Better solution: " , maxAreaRectangle2(arr))

