class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if len(st) > 0 and ((char == ')' and st[-1] == '(') \
            or (char == '}' and st[-1] == '{') \
            or (char == ']' and st[-1] == '[')):
                st.pop()
                continue
            
            st.append(char)
        
        return len(st) == 0