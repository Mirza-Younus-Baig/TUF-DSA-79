# find the element list that have the sum equal to target

arr = [2, 4,5,6,1,5,5,3,5,7,8]
target = 10

# Index hashing
mapping = dict()
for ind, val in enumerate(arr):
    if val in mapping:
        mapping[val].append(ind)
    else:
        mapping[val] = [ind]

arr.sort()
i = 0
j = len(arr) - 1

res = []
resInd = []

while i < j:
    if arr[i] + arr[j] == target:
        res.append([arr[i], arr[j]])
        resInd.append([mapping[arr[i]].pop(), mapping[arr[j]].pop()])
        i += 1
        j -= 1

    elif arr[i] + arr[j] < target:
        i += 1
    elif arr[i] + arr[j] > target:
        j -= 1

print(res)
print(resInd)


