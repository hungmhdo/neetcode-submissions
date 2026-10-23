class Solution:
    def trap(self, height: List[int]) -> int:
        # while len(height) != 0 and (height[0] == 0 or (len(height) > 1 and height[0] <= height[1])):
        #     height = height[1:]
        
        # while len(height) != 0 and (height[len(height) - 1] == 0 or (len(height) > 1 and height[len(height)-1] <= height[len(height)-2])):
        #     height = height[:len(height)-1]
        
        # if len(height) == 0:
        #     return 0
        
        # n = len(height)
        # heightL = [0] * n
        # heightR = [0] * n

        # for i in range(n):
        #     heightL[i] = max(height[i], heightL[i-1])
        #     heightR[n-i-1] = max(heightR[(n-i)%n], height[n-i-1])
        
        # total = 0
        # for i in range(n):
        #     total += min(heightL[i], heightR[i]) - height[i]
                
        # return total

        if not height:
            return 0
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res
        