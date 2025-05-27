# **Java Learning - Day 1**

## **Topics Covered**

### **1.**

### **Java Operators**

- **Arithmetic**: +, -, *, /, %
- **Relational**: ==, !=, >, <, >=, <=
- **Logical**: &&, ||, !
- **Assignment**: =, +=, -=, *=, /=, %=
- **Unary**: +, -, ++, --, !
- **Bitwise**: &, |, ^, ~, <<, >>, >>>
- **Ternary**: (condition) ? trueValue : falseValue
- **Instanceof** and **Type Cast**

### **2.**

### **Variable Types in Java**

- **Local Variables**: Declared inside methods; must be initialized before use.
- **Instance Variables**: Declared in the class but outside methods; belong to objects.
- **Static Variables (Class Variables)**: Declared with static; shared among all instances.

### **3.**

### **User Input using Scanner**

```
Scanner sc = new Scanner(System.in);
int num = sc.nextInt();
String word = sc.next();
sc.close();
```

### **4.**

### **Input an Array of Integers**

```
int[] arr = new int[n];
for (int i = 0; i < n; i++) {
    arr[i] = sc.nextInt();
}
```

### **5.**

### **Calling Methods from main()**

- Use static keyword to call directly.
- Use object reference for non-static methods:

```
ClassName obj = new ClassName();
obj.method();
```

### **6.**

### **Reverse an Array**

```
void reverseArray(int left, int right) {
    while (left < right) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}
```

### **7.**

### **Next Permutation Algorithm**

- Find pivot index where arr[i-1] < arr[i]
- Swap arr[ind - 1] with the smallest number > it in the right side
- Sort the right subarray:

```
Arrays.sort(arr, ind, arr.length);
```

### **8.**

### **Clean Code Improvements**

- Used Integer.MAX_VALUE instead of magic numbers like 99999
- Closed Scanner to avoid resource leaks

---

## **Next Steps**

- Handle multiple test cases
- Explore ArrayList and Collections
- Recursion and Dynamic Programming in Java

---

**Great work today!**
