from is_anagram import Solution


def test():
    solution = Solution()
    assert solution.isAnagram("anagram", "nagaram")
    assert not solution.isAnagram("rat", "car")
    assert not solution.isAnagram("ab", "a")
    print("All tests passed!")


if __name__ == "__main__":
    test()
