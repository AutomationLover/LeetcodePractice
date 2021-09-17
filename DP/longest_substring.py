# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_position_map = dict()
        max_length = cur_length = 0
        last_pos = -1
        for index, letter in enumerate(s):
            cur_length = index - last_pos
            if letter_position_map.get(letter, -2) > last_pos:
                cur_length = index - letter_position_map[letter] - 1
                last_pos = letter_position_map[letter]

            letter_position_map[letter] = index
            max_length = max(cur_length, max_length)
        return max_length

def test():
    s = "abcabcbb"
    sol = Solution()
    ans = sol.lengthOfLongestSubstring(s)
    assert ans == 3
    s = " "
    ans = sol.lengthOfLongestSubstring(s)
    assert ans == 1
    s = "pwwkew"
    ans = sol.lengthOfLongestSubstring(s)
    assert ans == 3
