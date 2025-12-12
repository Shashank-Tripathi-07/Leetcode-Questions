# 4. Median of Two Sorted Arrays
""" 
A Leetcode Hard Question 

Question: 
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106






It is particularly visible from the time complexity that we have to use something that gets the job done in binary time. The algorithm should be divide and conquer for this.
I tried binary search for this as it could solve the solution better and it worked. 
The solution I share here is the 3rd version (a very optimized one) 

Run Time: 1 ms | Beats 63.20% 
Memory: 17.82 MB | Beats 97.19%  {Classic Python case} 

Here's the solution
""" 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        a, b = nums1, nums2
        m, n = len(a), len(b)
        half = (m + n + 1) // 2
        lo, hi = 0, m

        INF = float('inf')
        NINF = -INF

        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            L1 = NINF if i == 0 else a[i - 1]
            R1 =  INF if i == m else a[i]
            L2 = NINF if j == 0 else b[j - 1]
            R2 =  INF if j == n else b[j]

            if L1 <= R2 and L2 <= R1:
                if (m + n) & 1:
                    return max(L1, L2)
                return (max(L1, L2) + min(R1, R2)) / 2

            if L1 > R2:
                hi = i - 1
            else:
                lo = i + 1
