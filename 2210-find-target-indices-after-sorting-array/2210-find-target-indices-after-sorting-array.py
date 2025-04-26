class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        arr = []
        for i in range(n):
            if sorted_nums[i] == target:
                arr.append(i)
        return arr         