class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        maxL = 0
        maxR = 0

        answer = 0

        while l < r:

            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                answer += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                answer += maxR - height[r]

        return answer
        