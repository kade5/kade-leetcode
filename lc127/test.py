from contains_duplicates import Solution


def test():
    solution = Solution()
    test_1 = [1, 2, 3, 1]
    assert solution.containsDuplicate(test_1)
    test_2 = [1, 2, 3, 4]
    assert not solution.containsDuplicate(test_2)
    test_3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert solution.containsDuplicate(test_3)


if __name__ == "__main__":
    test()
