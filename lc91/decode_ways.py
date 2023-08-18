class Solution:
    mapping = {}

    def numDecodings(self, s: str) -> int:
        memory = {len(s): 1}
        self.buildMapping()

        def decodeString(i):
            if i in memory:
                return memory[i]

            if s[i] == "0":
                return 0

            count = decodeString(i + 1)
            if i + 1 < len(s) and self.isValid(s[i : i + 2]):
                count += decodeString(i + 2)

            memory[i] = count
            return count

        return decodeString(0)

    def buildMapping(self):
        for i in range(ord("A"), ord("Z") + 1):
            self.mapping[str(i - ord("A") + 1)] = chr(i)

    def isValid(self, num):
        if num in self.mapping:
            return True
        return False
