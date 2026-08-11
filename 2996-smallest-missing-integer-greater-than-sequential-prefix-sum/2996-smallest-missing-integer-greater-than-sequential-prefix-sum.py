class Solution(object):
    def missingInteger(self, nums):
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        while True:
            if total not in nums:
                return total
            total += 1