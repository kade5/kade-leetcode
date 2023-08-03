class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        results = []
        word = ""
        nums = self.buildNumberMapping()

        def addCombination(i):
            nonlocal word
            if i >= len(digits):
                results.append(word)
                return
            for j in range(i, len(digits)):

                for letter in nums[int(digits[j])]:
                    word += letter
                    addCombination(j + 1)
                    word = word[:-1]

        if len(digits) > 0:
            addCombination(0)
        return results


    def buildNumberMapping(self) -> list[list[str]]:
        nums = [ [] for _ in range(10)]
        nums[2] = ['a', 'b', 'c']
        nums[3] = ['d', 'e', 'f']
        nums[4] = ['g', 'h', 'i']
        nums[5] = ['j', 'k', 'l']
        nums[6] = ['m', 'k', 'l']
        nums[7] = ['p', 'q', 'r', 's']
        nums[8] = ['t', 'u', 'v']
        nums[9] = ['w', 'x', 'y', 'z']

        return nums
