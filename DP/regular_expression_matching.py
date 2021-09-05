# https://leetcode.com/problems/regular-expression-matching/

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        # .*, .*

        def findmatch(s, p, m, n):
            if (s[:m] == p[:n]):
                return True

            if (m > 0 and n == 0):
                return False

            if (m == 0 and n > 0):
                if (p[n - 1] == '*'):
                    return findmatch(s, p, m, n - 2)
                return False

            if (s[m - 1] == p[n - 1] or p[n - 1] == '.'):
                return findmatch(s, p, m - 1, n - 1)

            elif (p[n - 1] == '*'):
                if (findmatch(s, p, m, n - 2)):  # if * means 0 time
                    return True
                if (s[m - 1] == p[n - 2]):  # if * means >1 times , then move on s
                    return findmatch(s, p, m - 1, n)
                if ((s[m - 1] != p[n - 2]) and p[n - 2] == '.'):
                    return findmatch(s, p, m - 1, n)
                return False

            return False

        return findmatch(s, p, m, n)


def test():

    sol = Solution()

    s = "aa"
    p = "a"
    ans = sol.isMatch(s, p)
    assert ans is False
    s = "aa"
    p = "a*"
    ans = sol.isMatch(s, p)
    assert ans is True
