class Solution:
    def checkValidString(self, s: str) -> bool:
        left_count = 0
        right_count = 0
        star_count = 0
        star_char = "("
        for c in s:
            if c == "(":
                left_count += 1
            if c == ")":
                right_count += 1
            if c == "*":
                star_count += 1

        used_stars = abs(left_count - right_count)

        if used_stars > star_count:
            return False

        if left_count > right_count:
            star_char = ")"

        stack = []

        for c in s:
            if c == "*":
                if used_stars > 0:
                    used_stars -= 1
                    c = star_char
                else:
                    continue

            if c == "(":
                stack.append(c)
            else:
                if not stack:
                    return False
                stack.pop()

        if not stack:
            return True

        return False
