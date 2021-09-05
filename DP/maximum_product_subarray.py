# https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = prev_max_prod = prev_neg_max_prod = nums[0]

        for i in range(1, len(nums)):
            prev_max_prod, prev_neg_max_prod = \
                max(nums[i],
                    nums[i] * prev_max_prod,
                    nums[i] * prev_neg_max_prod), \
                min(nums[i],
                    nums[i] * prev_max_prod,
                    nums[i] * prev_neg_max_prod)

            max_prod = max(max_prod, prev_max_prod)
        return max_prod

def test():
    nums = [2, 3, -2, 4]
    s = Solution()
    ans = s.maxProduct(nums)
    assert ans == 6