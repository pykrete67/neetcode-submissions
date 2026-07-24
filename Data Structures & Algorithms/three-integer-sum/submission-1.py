class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        answer = []

        for index, n in enumerate(nums):

            if index > 0 and n == nums[index - 1]:
                continue

            l = index + 1
            r = len(nums) - 1

            while l < r:
                summ = nums[l] + nums[r]
                target = 0 - n

                if (summ > target):
                    r -= 1
                if (summ < target):
                    l += 1
                if (summ == target):
                    # return [[n, nums[l+1], nums[r]]]
                    answer.append([n, nums[l], nums[r]])
                    # break
                    l += 1
                    r -= 1
                    
                    # skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return answer
        