//Given an array of integers, return indices of the two numbers such that they add up to a specific target.

//You may assume that each input would have exactly one solution, and you may not use the same element twice.

//Example:

//Given nums = [2, 7, 11, 15], target = 9,

//Because nums[0] + nums[1] = 2 + 7 = 9,
//return [0, 1].


class Solution {
    public int[] twoSum(int[] nums, int target) {
        //1,5,6,2,6,7 --> 8
        int[] result = new int[2];
        Map<Integer, Integer> lookUp = new HashMap<>();
        for(int i = 0; i < nums.lenght; i+=) {
            if(lookUp.containsKey(nums[i])) {
                result[0] = i;
                result[1] = lookUp.get(nums[i]);
            } else {
                lookUp.put(target - nums[i], i);
            }
        }
        return result;
}
