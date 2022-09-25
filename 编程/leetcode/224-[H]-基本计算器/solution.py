class Solution:

    def calculate(self, s: str) -> int:
        stack = []
        def valid(c):
            if c not in ('+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '/', '(', ')'):
                return False
            return True
        
        for c in s:
            
