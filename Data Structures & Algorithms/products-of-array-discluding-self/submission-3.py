class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # array a and array b
        # array a[i] = product of all elements from 0 -> i
        # array b[i] = product of all elements from i -> len(nums)
        n = len(nums)
        a = [nums[0]] * n
        b = [nums[n-1]] * n

        for i in range(1, n):
            a[i] = a[i-1] * nums[i]
            b[n-i-1] = b[n-i] * nums[n-i-1]
        
        a = [1] + a + [1]
        b = [1] + b + [1]
        product = []
        
        for i in range(1,n+1):
            product.append(a[i-1] * b[i+1])
        return product