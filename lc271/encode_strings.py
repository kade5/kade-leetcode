class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        delimeter = "|"
        for word in strs:
            len_word = str(len(word))
            encoded_str = encoded_str + len_word + delimeter + word
        return encoded_str

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, encoded_str):
        decoded_list = []
        delimeter = "|"
        i = 0
        while i < len(encoded_str):
            start = i
            while encoded_str[i] != delimeter:
                i += 1
            word_length = int(encoded_str[start:i])
            i += 1
            word = encoded_str[i:i+word_length]
            decoded_list.append(word)
            i += word_length
        return decoded_list
