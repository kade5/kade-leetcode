class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        neq_count = 0
        first_diff_idx = 0
        second_diff_idx = 0

        for i in range(n):
            if s1[i] != s2[i]:
                neq_count += 1
                if neq_count == 1:
                    first_diff_idx = i
                elif neq_count == 2:
                    second_diff_idx = i
            if neq_count > 2:
                return False

        swap_ind = s1[first_diff_idx] == s2[second_diff_idx] and s1[second_diff_idx] == s2[first_diff_idx]

        return (neq_count == 2 and swap_ind) or neq_count == 0

