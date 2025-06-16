

✅ Topics Covered

1. Stack Concepts
	•	LIFO (Last In First Out)
	•	Common operations: push, pop, peek, isEmpty, isFull, printStack

2. Stack Implementation Without Built-in Classes
	•	Built a custom stack using an array
	•	Defined fields: arr[], top, size
	•	Implemented constructor to initialize stack with custom size

⸻

🔧 Methods Implemented

✅ push(int val)
	•	Adds element to the top of the stack
	•	Handles overflow condition

✅ pop()
	•	Removes and returns top element
	•	Decrements top pointer
	•	Returns -1 if stack is empty

✅ peek()
	•	Returns the top element without removing it
	•	Returns -1 if stack is empty

✅ isEmpty()
	•	Returns true if stack is empty

⸻

🧠 Key Learnings
	•	How Java handles class members (this.arr vs arr)
	•	Why top-- is necessary in pop() to actually remove an item
	•	Difference between boolean (Java) and bool (C++)
	•	How using namespace works in C++ and Java’s lack of direct pointers
