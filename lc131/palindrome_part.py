class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        current_part = []

        def checkPartition(i):
            if i >= len(s):
                result.append(current_part.copy())
                return
            for j in range(i, len(s)):
                if self.checkPalindome(s[i:j + 1]):
                    current_part.append(s[i:j + 1])
                    checkPartition(j + 1)
                    current_part.pop()

        checkPartition(0)
        return result

        

    def checkPalindome(self, word):
            i = 0
            j = len(word) - 1
            
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1
            return True
        
