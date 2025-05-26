import java.util.Scanner;
import java.util.Arrays;

class next_permutation{
    int[] arr;

    public static void main(String args[]){
        System.out.println("Enter the number of elements");
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();

        next_permutation np = new next_permutation();
        np.arr = new int[size];
        System.out.println("Enter the elements of the array");
        for(int i = 0; i < size; i++) {
            np.arr[i] = sc.nextInt();
        }

        // Optionally call the perm method
        int[] result = np.perm();
        System.out.println(Arrays.toString(result));

        sc.close();
    }

    void reverseArray(int left, int right) {
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }

    int[] perm() {
        int ind = 0;
        for(int i = arr.length - 1; i > 0; i-- ){
            if(arr[i-1] < arr[i]){
                ind = i;
                break;
            }
        }
        if(ind == 0){
            reverseArray(0, arr.length - 1);
            return arr;
        }

        int nextGreater = Integer.MAX_VALUE;
        int maxInd = ind;
        for (int i = ind; i < arr.length; i++) {
            if (arr[i] > arr[ind - 1] && arr[i] < nextGreater) {
                nextGreater = arr[i];
                maxInd = i;
            }
        }
        int temp = arr[ind - 1];
        arr[ind - 1] = arr[maxInd];
        arr[maxInd] = temp;


        Arrays.sort(arr,ind, arr.length);
        
        return arr;

    }
}