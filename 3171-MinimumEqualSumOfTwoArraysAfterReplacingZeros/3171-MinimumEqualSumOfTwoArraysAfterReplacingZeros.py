# Last updated: 4/15/2026, 11:49:23 PM
class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        one_sum = 0
        two_sum = 0
        one_replaceable = False
        two_replaceable = False
        for i in range(len(nums1)):
            if nums1[i] == 0:
                nums1[i] = 1
                one_replaceable = True
            one_sum += nums1[i]
        for j in range(len(nums2)):
            if nums2[j] == 0:
                nums2[j] = 1
                two_replaceable = True
            two_sum += nums2[j]
        if one_sum > two_sum and not two_replaceable or two_sum > one_sum and not one_replaceable: 
            return -1 
        return max(one_sum, two_sum)
        
        

                