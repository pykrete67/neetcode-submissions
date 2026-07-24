class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for index, item in enumerate(nums):
            dif = target - item

            if dif in temp:
                return([temp[dif], index])
            
            temp[item] = index

        
        
        # temp = set(nums)

        # for i in range(len(nums)):
        #     if (target - nums[i]) in temp:
        #         try:
        #             j = nums.index(target - nums[i], i+1, len(nums))
        #             return([i, j])
        #         except ValueError:
        #             continue