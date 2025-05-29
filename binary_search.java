import java.util.Scanner;


class binary_search {
    

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int mid;

        while (left <= right) {
            mid = (left + right) / 2;

            if (nums[mid] == target)
                return mid;
            else if (nums[mid] < target)
                left = mid + 1;
            else
                right = mid - 1;
        }

        return -1;
    }
    public static void main(String args[]){
        int n;
        System.out.println("Enter the length of the array");
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        System.out.println("Enter " + n +" elements");
        int[] nums = new int[n];
        for(int i =0; i< n; i++){
            nums[i] = sc.nextInt();
        }

        System.out.println("Enter the target to find");
        int target = sc.nextInt();

        binary_search bs = new binary_search();
        int result = bs.search(nums, target);
        System.out.println("Target found at index: " + result);
        sc.close();
        
    }
}