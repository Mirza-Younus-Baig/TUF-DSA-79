class Solution:
    def nextLargerElement(self, arr):
        stack = []
        nge = []

        for i in range(len(arr) - 1, -1, -1):
            
            while stack and arr[i] >= stack[-1] :
                stack.pop()
            
            if stack:
                nge.append(stack[-1])
            else:
                nge.append(-1)

            stack.append(arr[i])
        
        return nge[::-1] 


if __name__ == "__main__":
    arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
    sol = Solution()
    result = sol.nextLargerElement(arr)
    print("Next Greater Elements:", result)