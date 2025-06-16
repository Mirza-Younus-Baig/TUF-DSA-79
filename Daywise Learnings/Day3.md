Java & DSA Wrap-Up

✅ Topics Covered

1. Search in Rotated Sorted Array (No Duplicates)
	•	Implemented binary search to find a target in a rotated sorted array with distinct elements.
	•	Handled sorted/rotated halves by checking:

if nums[left] <= nums[mid]:
    # left half sorted
else:
    # right half sorted

	•	Returned the index of the target if found, else -1.

🔍 Example:

nums = [4,5,6,7,0,1,2], k = 0 → Output: 4
nums = [5,1,3], k = 5 → Output: 0


⸻

2. Search with Duplicates Allowed
	•	Learned why extra checks are needed when elements are duplicated.
	•	Used logic:

if nums[left] == nums[mid] == nums[right]:
    left += 1
    right -= 1

	•	This avoids infinite loops when array contains many duplicates.

⸻

3. Binary Search Recap
	•	Reinforced standard binary search template:

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    ...

	•	Practiced binary search as a subroutine in rotated sorted search.

⸻

🧠 Concepts Reinforced
	•	Binary search with conditions on sorted halves
	•	Edge cases like [5, 1, 3]
	•	Search failure due to incorrect range check
	•	Search with and without duplicates

⸻

✅ What’s Next
	•	Convert this logic to Java and test
	•	Add recursive version
	•	Practice related problems: Find Minimum in Rotated Sorted Array, Search Range, etc.

⸻
