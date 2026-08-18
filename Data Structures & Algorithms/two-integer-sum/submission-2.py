class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i, n in enumerate(nums):
            if target-n in mapping:
                return [mapping[target-n], i]
            else:
                mapping[n] = i



# 1 - naive - nested for loop search - O(n^2)

# 2 - hashmap
# for each value, check adn store the diff in hashmap{diff:idx}
