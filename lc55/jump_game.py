class Solution:
    def canJump(self, nums: list[int]) -> bool:
        can_jump = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] - (len(nums) - i - 1) >= 0:
                can_jump.add(i)
            else:
                for j in range(nums[i], 0, -1):
                    if j + i in can_jump:
                        can_jump.add(i)
                        break

        return 0 in can_jump
