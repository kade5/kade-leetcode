class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        new_string = s
        for shift_one in shift:
            new_string = self.single_shift(new_string, shift_one)

        return new_string

    @staticmethod
    def single_shift(s: str, shift: list[int]) -> str:
        len_s = len(s)
        shift_amount = shift[1] % len_s
        if shift[0] == 0:
            return s[shift_amount:len_s] + s[:shift_amount]
        else:
            return s[len_s - shift_amount:len_s] + s[:len_s - shift_amount]
