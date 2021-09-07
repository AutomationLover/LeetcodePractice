# https://leetcode.com/problems/regular-expression-matching/
class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def islettermatch(si, pi):
            return si == pi or pi == '.'

        def findmatch(s, p, sn, pn):
            if pn < 0 or sn < 0:
                return False

            if s[:sn] == p[:pn]:
                return True

            if sn > 0 and pn == 0:
                return False

            if sn == 0 and pn > 0:
                if p[pn - 1] != '*':
                    return False
                return findmatch(s, p, sn, pn - 2)

            if islettermatch(s[sn - 1], p[pn - 1]):
                return findmatch(s, p, sn - 1, pn - 1)

            # sn > 0 and pn > 0
            if p[pn - 1] == '*':
                if findmatch(s, p, sn, pn - 2):  # remove x*, if the rest can match
                    return True
                if islettermatch(s[sn - 1], p[pn - 2]):  # match s with letter before * in p, till not match
                    return findmatch(s, p, sn - 1, pn)

            return False

        return findmatch(s, p, len(s), len(p))


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def islettermatch(si, pi):
            return si == pi or pi == '.'

        def findmatch(s, p, sn, pn):
            if pn < 0 or sn < 0:
                return False

            if s[:sn] == p[:pn]:
                return True

            if pn == 0: #sn > 0 and
                return False

            if sn == 0: # and pn > 0
                if p[pn - 1] != '*':
                    return False
                return findmatch(s, p, sn, pn - 2)

            if islettermatch(s[sn - 1], p[pn - 1]):
                return findmatch(s, p, sn - 1, pn - 1)

            if p[pn - 1] == '*':
                if findmatch(s, p, sn, pn - 2):  # remove x*, if the rest can match
                    return True
                if islettermatch(s[sn - 1], p[pn - 2]):  # match s with letter before * in p, till not match
                    return findmatch(s, p, sn - 1, pn)

            return False

        return findmatch(s, p, len(s), len(p))


def test2():

    sol = Solution2()

    s = "aa"
    p = "a"
    ans = sol.isMatch(s, p)
    assert ans is False
    s = "aa"
    p = "a*"
    ans = sol.isMatch(s, p)
    assert ans is True
    s = "aab"
    p = "c*a*b"
    ans = sol.isMatch(s, p)
    assert ans is True
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
    s = "aab"
    p = "c*a*b"
    ans = sol.isMatch(s, p)
    assert ans is True