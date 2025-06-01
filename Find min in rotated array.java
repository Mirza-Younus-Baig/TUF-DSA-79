
import java.util.Scanner;

class Solution {
    public int findMin(int[] nums) {
        if(nums.length < 2)
            return nums[0];
        int left = 0, right = nums.length - 1;

        while(left <= right ){
            int mid = (left + right) / 2;
            if(nums[mid] >= nums[right])
                left = mid + 1;
            else
                right = mid;
        }
        return nums[right];
    }
    public static void main(String[] args) {
        Solution sln = new Solution();
        Scanner sc = new Scanner(System.in);
        int n;
        System.out.println("Enter the size of the array");
        n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter " + n + " elements");
        for(int i=0; i<n; i++)
            arr[i] = sc.nextInt();
        
        int res = sln.findMin(arr);

        System.out.println("Min element in the array is " + res);
        
    }
}

