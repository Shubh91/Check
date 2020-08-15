//Given a string, find the length of the longest substring without repeating characters.

//Example 1:

//Input: "abcabcbb"
//Output: 3 
//Explanation: The answer is "abc", with the length of 3. 
//Example 2:

//Input: "bbbbb"
//Output: 1
//Explanation: The answer is "b", with the length of 1.
//Example 3:

//Input: "pwwkew"
//Output: 3
//Explanation: The answer is "wke", with the length of 3. 
//             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


  class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 1):
            return 1
        maxSubstring = 0
        print (len(s))
        for i in range(0, len(s)): 
            temp = s[i]
            currentSubstringLen = len(temp)
            for j in range(i+1, len(s), 1):
                if (s[j] not in temp):
                    temp = temp + s[j]
                    currentSubstringLen = len(temp)
                    if (currentSubstringLen >= maxSubstring):
                        maxSubstring = currentSubstringLen
                else:
                    if (currentSubstringLen >= maxSubstring):
                        maxSubstring = currentSubstringLen
                    break
        return maxSubstring
