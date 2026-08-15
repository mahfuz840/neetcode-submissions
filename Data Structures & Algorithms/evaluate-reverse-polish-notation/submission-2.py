class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                num2 = st.pop()
                num1 = st.pop()
                st.append(self.processOperation(num1, num2, token))
            else:
                st.append(int(token))
            
        return st.pop()

    def processOperation(self, num1, num2, operator) -> int:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        return int(num1 / num2)