class Solution {
    public int maxArea(int[] height) {
        //
        int maxVolumeSoFar = 0, l = 0, r = height.length -1;
        while(l < r) {
            maxVolumeSoFar = Math.max(maxVolumeSoFar, Math.min(height[l], height[r])*(r-l));
            if(height[l] <= height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxVolumeSoFar;
    }
}
