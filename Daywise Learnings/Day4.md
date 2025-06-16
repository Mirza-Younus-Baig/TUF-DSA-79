# Java LinkedList Methods - Quick Reference

| Method                    | What it does                                               |
|---------------------------|------------------------------------------------------------|
| `add(E e)`                | Adds element to the end                                    |
| `add(int index, E e)`     | Inserts element at specific index                          |
| `addFirst(E e)`           | Adds element to the front                                  |
| `addLast(E e)`            | Adds element to the end                                    |
| `offer(E e)`              | Queue-style add to end                                     |
| `offerFirst(E e)`         | Queue-style add to front                                   |
| `offerLast(E e)`          | Queue-style add to end                                     |
| `remove()`                | Removes and returns first element                          |
| `remove(int index)`       | Removes element at given index                             |
| `removeFirst()`           | Removes first element                                      |
| `removeLast()`            | Removes last element                                       |
| `poll()`                  | Retrieves and removes first element (null if empty)        |
| `pollFirst()`             | Retrieves/removes first (null if empty)                    |
| `pollLast()`              | Retrieves/removes last (null if empty)                     |
| `get(int index)`          | Gets element at index                                      |
| `getFirst()`              | Gets first element                                         |
| `getLast()`               | Gets last element                                          |
| `peek()`                  | Peeks at first element without removing                    |
| `peekFirst()`             | Peeks at first                                             |
| `peekLast()`              | Peeks at last                                              |
| `set(int index, E e)`     | Replaces element at index                                  |
| `contains(Object o)`      | Checks if element exists                                   |
| `indexOf(Object o)`       | Index of first occurrence                                  |
| `lastIndexOf(Object o)`   | Index of last occurrence                                   |
| `size()`                  | Returns number of elements                                 |
| `isEmpty()`               | Checks if list is empty                                    |
| `clear()`                 | Removes all elements                                       |
| `iterator()`              | Returns iterator for loop-based traversal                  |
| `descendingIterator()`    | Returns reverse iterator                                   |


`
import java.util.LinkedList;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        // 1. Create and initialize
        LinkedList<Integer> list = new LinkedList<>();

        // 2. Add elements
        list.add(10);
        list.addFirst(5);
        list.addLast(15);
        list.add(1, 7);  // Insert 7 at index 1

        System.out.println("Original list: " + list);

        // 3. Access elements
        System.out.println("First element: " + list.getFirst());
        System.out.println("Last element: " + list.getLast());
        System.out.println("Element at index 2: " + list.get(2));

        // 4. Remove elements
        list.removeFirst();
        list.removeLast();
        list.remove(1);  // Remove element at index 1
        System.out.println("After removals: " + list);

        // 5. Special methods
        System.out.println("List contains 10? " + list.contains(10));
        System.out.println("Size of list: " + list.size());
        list.set(0, 100);  // Replace first element with 100
        System.out.println("After set(0, 100): " + list);

        // 6. Using iterator
        System.out.print("Iterating over list: ");
        Iterator<Integer> it = list.iterator();
        while (it.hasNext()) {
            System.out.print(it.next() + " ");
        }
        System.out.println();
    }
}
`