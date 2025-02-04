class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        n = len(num_str)
        max_right_idx = [0] * n
        cur_max = (n - 1, int(num_str[n - 1]))

        for i in range (n - 1, -1, -1):
            if int(num_str[i]) > cur_max[1]:
                cur_max = (i, int(num_str[i]))

            max_right_idx[i] = cur_max[0]

        for i, digit in enumerate(max_right_idx):
            if int(num_str[i]) < int(num_str[max_right_idx[i]]):
                num_str = self.swap_digit(num_str, i, max_right_idx[i])
                break

        return int(num_str)

    def swap_digit(self, num: str, pos1: int, pos2: int):
        num_list = list(num)
        swap = num_list[pos1]
        num_list[pos1] = num[pos2]
        num_list[pos2] = swap

        return ''.join(num_list)
