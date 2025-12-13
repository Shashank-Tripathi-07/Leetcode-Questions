"""
3. Longest Substring Without Repeating Characters

A Leetcode Medium question 

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

INSIGHTS: 
I built a raw version that gave me a runtime of around 20ms. This solution here takes just 7ms . Often times, it's funny to see how changing up the variable names and spaces can reduce runtimes.... lol

""" 


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ci = {}                     # last index of each character
        l = 0                       # left pointer
        max_len = 0                 # answer

        get = ci.get                # LOCAL BIND (eliminates repeated attribute lookups)

        for r, ch in enumerate(s):
            prev = get(ch, -1)      # single dictionary access (FASTEST WAY)
            if prev >= l:
                l = prev + 1

            ci[ch] = r              # update last seen index

            # manual max() (avoids function call)
            length = r - l + 1
            if length > max_len:
                max_len = length

        return max_len

# Runtime: 7ms | Beats 99.17%
# Memory: 18.01 MB | Beats 11.80% 


# This solution uses a sliding window algorithm to get the result. I got the idea to use it from the discussions whilst optimizing the code. We can also do it in the  O(n^2) manner. 
# Here's the solution in the slower and more usual manner 


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        
        # Try starting from each position
        for i in range(len(s)):
            seen = set()  # Track characters in current substring
            current_len = 0
            
            # Build substring from position i
            for j in range(i, len(s)):
                # If we hit a duplicate, stop this substring
                if s[j] in seen:
                    break
                
                # Add character and increase length
                seen.add(s[j])
                current_len += 1
            
            # Update max if this substring is longer
            max_len = max(max_len, current_len)
        
        return max_len


# Runtime: 255 ms | Beats 8.14% 
# Memory: 17.85 MB | Beats 52.14% 

