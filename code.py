class Solution(object):
    def sortedArrayToBST(self, nums):
        def bst(s, e): #start , end
            if s < e:
                mi = s + (e - s) // 2
                return TreeNode(
                               val = nums[mi], 
                               left = bst(s, mi),
                               right = bst(mi + 1, e))
        return bst(0, len(nums))
