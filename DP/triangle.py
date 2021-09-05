# https://leetcode.com/problems/triangle/

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        height = len(triangle)
        if height == 1:
            return triangle[0][0]
        for h in range(1, height):
            last_layer = triangle[h-1]
            cur_layer = triangle[h]
            cur_layer[0] += last_layer[0]
            cur_layer[-1] += last_layer[-1]
            for i in range(1, h):
                cur_layer[i] += min(last_layer[i], last_layer[i-1])
        return min(triangle[-1])

def test():
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    s = Solution()
    ans = s.minimumTotal(triangle)
    assert ans == 11