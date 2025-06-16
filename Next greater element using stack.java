import java.util.Scanner;

class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements");

        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        myStack stack = new myStack(n);
        int[] result = new int[n];

        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= arr[i]) {
                stack.pop();
            }

            result[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(arr[i]);
        }

        System.out.println("Next Greater Elements:");
        for (int val : result)
            System.out.print(val + " ");
    }
}