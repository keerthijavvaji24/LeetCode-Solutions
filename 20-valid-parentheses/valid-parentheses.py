class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        if len(s)==1:return False
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                elif d[ch]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False

    
              