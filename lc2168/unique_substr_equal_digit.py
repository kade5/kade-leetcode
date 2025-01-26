class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        unique_substrings = set()
        size_s = len(s)

        for start in range(size_s):
            digit_count = [0] * 10

            for end in range(start, size_s):
                digit_count[int(s[end])] += 1

                common_frequency = 0
                is_valid = True

                for count in digit_count:
                    if count == 0:
                        continue
                    elif common_frequency == 0:
                        common_frequency = count
                    elif common_frequency != count:
                        is_valid = False
                        break

                if is_valid:
                    unique_substrings.add(s[start:end + 1])


        return len(unique_substrings)
