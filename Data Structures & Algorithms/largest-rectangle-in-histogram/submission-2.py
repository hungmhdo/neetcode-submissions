class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # area = max(max(heights), n * min(heights))
        # for i in range(n - 1):
        #     for j in range(i+1, n):
        #         currMin = heights[i]
        #         for k in range(i, j+1):
        #             currMin = min(currMin, heights[k])
                
        #         area = max(area, currMin * (j-i+1))
        
        # return area

        l = [0] * n
        r = [0] * n
        stack = [0]

        for i in range(1, n):
            if heights[i] > heights[i-1]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    l[i] += l[stack[-1]] + 1
                    stack.pop()
                stack.append(i)
        
        stack = [n-1]
        for i in range(n - 2, -1, -1):
            if heights[i] > heights[i+1]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    r[i] += r[stack[-1]] + 1
                    stack.pop()
                stack.append(i)

        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, (l[i] + r[i] + 1) * heights[i])
        return maxArea


# 3222221