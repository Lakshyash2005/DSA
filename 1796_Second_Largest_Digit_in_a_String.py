# LeetCode 1796 - Second Largest Digit in a String
class Solution:
    def secondHighest(self, s: str) -> int:
        l = -1
        sl = -1
        for ch in s:
            if ch.isdigit():
                d = int(ch)
                if d > l:
                    sl = l
                    l = d
                elif d < l and d > sl:
                    sl = d
        return sl
