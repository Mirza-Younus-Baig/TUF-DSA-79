import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();

        if (nums.length < 3)
            return res;

        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];

                if (total == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;

                    while (left < right && nums[left] == nums[left - 1]) left++;
                    while (left < right && nums[right] == nums[right + 1]) right--;
                } else if (total < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        int[][] testCases = {
            {-1, 0, 1, 2, -1, -4},
            {0, 0, 0, 0},
            {-2, 0, 0, 2, 2},
            {1, 2, 3, 4, 5},
            {-5, 2, 3, 0, -2, 1, 4, -1}
        };

        for (int[] testCase : testCases) {
            List<List<Integer>> result = solution.threeSum(testCase);
            System.out.println("Input: " + Arrays.toString(testCase));
            System.out.println("Triplets: " + result);
            System.out.println();
        }
    }
}