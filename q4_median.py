class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        n = []
        length = len(nums1) + len(nums2)
        l = int(length / 2)

        for p in range(l + 1):
            if p1 < len(nums1):
                if p2 < len(nums2):
                    if nums1[p1] < nums2[p2]:
                        if p >= l - 1:
                            n.append(nums1[p1])
                        p1 = p1 + 1
                    else:
                        if p >= l - 1:
                            n.append(nums2[p2])
                        p2 = p2 + 1
                else:
                    if p >= l - 1:
                        n.append(nums1[p1])
                    p1 = p1 + 1
            else:
                if p >= l - 1:
                    n.append(nums2[p2])
                p2 = p2 + 1

        if length % 2 == 1:
            return float(n[-1])
        else:
            return float(n[-1] + n[-2]) / 2.0 