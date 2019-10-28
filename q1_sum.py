class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {nums[0]: 0}
        i = 1
        for num in nums[1:]:
            target_temp = target - num
            if num_dict.get(target_temp) != None:
                return [num_dict[target_temp], i]

            num_dict[num] = i
            i = i + 1