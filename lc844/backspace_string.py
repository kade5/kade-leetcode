class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_pointer = len(s) - 1
        t_pointer = len(t) - 1
        sb = 0
        tb = 0

        while (s_pointer >= 0 and t_pointer >= 0) or ():
            if s[s_pointer] == "#":
                sb += 1
                s_pointer -= 1
            elif t[t_pointer] == "#":
                tb += 1
                t_pointer -= 1
            elif sb > 0:
                s_pointer -= 1
                sb -= 1
            elif tb > 0:
                t_pointer -= 1
                tb -= 1
            elif s[s_pointer] == t[t_pointer]:
                s_pointer -= 1
                t_pointer -= 1
            else:
                break

        return s_pointer == t_pointer == -1
