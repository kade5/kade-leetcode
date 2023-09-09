class Solution:
    def checkValidString(self, s: str) -> bool:
        left_count = 0
        right_count = 0
        star_count = 0
        for c in s:
            if c == "(":
                left_count += 1
            if c == ")":
                right_count += 1
            if c == "*":
                star_count += 1

            if (
                left_count < right_count + star_count
                and left_count + star_count < right_count
            ):
                return False

        if abs(left_count - right_count) > star_count:
            return False

        return True
