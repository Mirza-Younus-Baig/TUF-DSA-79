Day 8 - Java & DSA Wrap-Up

✅ Key Topics Covered

1. Two Sum Problem (Python)
	•	Learned how to find pairs in a list that sum to a target using the two-pointer technique.
	•	Optimized by sorting and maintaining a map of values to indices to retrieve original positions.

🔹 Example:

arr = [2, 4, 5, 1, 3]
target = 6
# Result: [[1, 3], [2, 4]] for pairs [5, 1], [3, 3] based on original indices


⸻

2. Three Sum Problem (Java)
	•	Implemented optimal O(n^2) solution using two-pointer approach.
	•	Handled duplicate elements to ensure unique triplets.
	•	Converted a working solution into a complete class with test cases in main.

🔹 Key Concepts:
	•	Sort the array
	•	Fix one index and use two pointers to find the other two
	•	Skip duplicates using while loops

🔹 Example Test Case:

Input: [-5, 2, 3, 0, -2, 1, 4, -1]
Output: [[-5, 1, 4], [-5, 2, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]


⸻

3. Matrix in Java
	•	Declared and accessed 2D arrays
	•	Built a custom Matrix class concept with methods like transpose(), add(), and print()

🔹 Syntax:

int[][] matrix = new int[3][3];
matrix[0][1] = 5;


⸻

4. ArrayList and List Interface
	•	Used ArrayList<ArrayList<Integer>> to create dynamic 2D lists
	•	Compared List (interface) vs ArrayList (implementation)

🔹 Dynamic 2D Array:

ArrayList<ArrayList<Integer>> matrix = new ArrayList<>();
matrix.add(new ArrayList<>(Arrays.asList(1, 2)));
matrix.add(new ArrayList<>(Arrays.asList(3, 4)));


⸻

🧠 Reinforced Concepts
	•	Java collection APIs (List, ArrayList, Arrays.asList())
	•	Two-pointer algorithm
	•	Sorting + Duplicate skipping
	•	Matrix structure in Java
	•	Writing readable, testable Java code

⸻

✅ Next Suggestions:
	•	Add support for 3Sum with custom target
	•	Implement matrix methods: multiplication, identity check
	•	Try sliding window and hashmap-based problems

⸻
