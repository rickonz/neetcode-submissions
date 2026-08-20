class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in num_set:
                streak = 1
                m = n + 1
                while m in num_set:
                    streak += 1
                    m += 1
                longest = max(longest, streak)
            else:
                continue
        return longest
        