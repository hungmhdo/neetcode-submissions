class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        st = []
        for c in tokens:
            if is_number(c):
                st.append(int(c))
            else:
                b = st.pop()
                a = st.pop()

                if c == "+":
                    st.append(a + b)
                
                if c == "-":
                    st.append(a - b)
                
                if c == "*":
                    st.append(a * b)
                
                if c == "/":
                    st.append(int(a / b))
        return st[-1]
