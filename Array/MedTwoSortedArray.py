class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        : The basic idea is to use binary search to separate these two array to leftpart and rightpart
        : We want all the elements in the leftpart are smaller than those in the right part
        : As these two array are sorted, we just need to comapre the FOUR element at the bounday
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, m, nums2, n = nums2, n, nums1, m
        start, end = 0, m
        hallen = (m + n + 1) / 2
        while start <= end:
            i = start + (end - start) / 2
            j = hallen - i
            if i < m and nums1[i] < nums2[j - 1]:
                start = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                end = i - 1
            else:
                if i == 0:
                    leftmax = nums2[j - 1]
                elif j == 0:
                    leftmax = nums1[i - 1]
                else:             
                    leftmax = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2:
                    return leftmax / 1.0   #we need to stop the while loop, here becasue j will be outof bound

                if i == m:
                    rightmin = nums2[j]
                elif j == n:
                    rightmin = nums1[i]
                else:
                    rightmin = min(nums1[i], nums2[j])

                return (leftmax + rightmin) / 2.0

model = Solution()
nums1 = []
nums2 = [1]
print model.findMedianSortedArrays(nums1, nums2)