class Solution:
    def countBits(self, n: int) -> list[int]:
        ones_list = [0]

        while len(ones_list) < n + 1:
            for i in range(len(ones_list)):
                ones_list.append(ones_list[i] + 1)
                if len(ones_list) > n:
                    break

        return ones_list
