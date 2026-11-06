class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time to get to target = target - position / speed

        st = []
        n = len(position)
        a = []

        for i in range(n):
            a.append((position[i], speed[i]))
        
        a = sorted(a)

        for i in range(n):
            time = (target - a[i][0]) / a[i][1]
            while st and st[-1] <= time:
                st.pop()
            
            st.append(time)
        return len(st)