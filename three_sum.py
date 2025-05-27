target = 0
# arr = [-1, 0, 1, 2, -1, -4]
# Expected Output: [[-1, -1, 2], [-1, 0, 1]]
# arr = [1, 2, 3, 4, 5]
# # Expected Output: []
# arr = [0, 0, 0, 0]
# # Expected Output: [[0, 0, 0]]
# arr = [-2, 0, 0, 2, 2]
# # Expected Output: [[-2, 0, 2]]
arr = [-5, 2, 3, 0, -2, 1, 4, -1]
# # Expected Output: [[-5, 1, 4], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]


if len(arr) < 3:
    print(False)
else:
    arr.sort()
    res = []

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = len(arr) - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == target:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif total < target:
                left += 1
            else:
                right -= 1

    print(res)

