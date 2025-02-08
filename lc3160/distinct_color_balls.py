from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        color_dict = defaultdict(int)
        ball_dict = defaultdict(int)
        colors = 0
        ans = []

        for ball, color in queries:
            old_color = ball_dict.get(ball, 0)
            if old_color == 0:
                ball_dict[ball] = color
                color_dict[color] += 1
                if color_dict[color] == 1:
                    colors += 1
            else:
                ball_dict[ball] = color
                color_dict[old_color] -= 1
                if color_dict[old_color] == 0:
                    colors -= 1
                color_dict[color] += 1
                if color_dict[color] == 1:
                    colors += 1

            ans.append(colors)

        return ans

