# Question - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        a, b = len(nums1), len(nums2)
        final = []

        while i<a and j<b:
            if nums1[i] < nums2[j]:
                final.append(nums1[i])
                i += 1
            else:
                final.append(nums2[j])
                j += 1

        if i<a:
            final.extend(nums1[i:])
        elif j<b:
            final.extend(nums2[j:])

        mid = len(final)//2
        print(mid)
        if len(final)%2!=0:
            return final[mid]
        else:
            return (final[mid-1]+final[mid])/2