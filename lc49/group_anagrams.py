class Solution(object):
    def groupAnagrams(self, strs: list[str]):
        """
        Given an array of strings strs, group the anagrams together.
        You can return the answer in any order.
                :type strs: List[str]
                :rtype: List[List[str]]
        """
        word_dict_dict = {}
        anagrams_list = []

        for i in range(len(strs)):
            char_dict = {}
            for character in strs[i]:
                char_dict[character] = 1 + char_dict.get(character, 0)
            word_dict_dict[strs[i]] = char_dict

        for i in range(len(strs)):
            added = False
            if not anagrams_list:
                anagrams_list.append([strs[i]])
            else:
                for j in range(len(anagrams_list)):
                    if word_dict_dict[strs[i]] == word_dict_dict[anagrams_list[j][0]]:
                        anagrams_list[j].append(strs[i])
                        added = True
                        break
                if not added:
                    anagrams_list.append([strs[i]])

        return anagrams_list

    def groupAnagramsRework(self, strs: list[str]):
        """
        Given an array of strings strs, group the anagrams together.
        You can return the answer in any order.
                :type strs: List[str]
                :rtype: List[List[str]]
        """
        word_dict = {}

        for i in range(len(strs)):
            char_array = [0] * 26
            for character in strs[i]:
                char_array[self.lowercase_value(character)] += 1

            anagram_hash = tuple(char_array)
            if not word_dict.get(anagram_hash):
                word_dict[anagram_hash] = [strs[i]]
            else:
                word_dict[anagram_hash].append(strs[i])

        return list(word_dict.values())

    def lowercase_value(self, character):
        return ord(character) - ord('a')

