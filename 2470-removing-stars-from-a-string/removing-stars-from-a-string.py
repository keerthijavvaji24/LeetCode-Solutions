class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        for i in s:
            # print(i)
            if i=="*":
                stk.pop(-1)
            else:
                stk.append(i)
        print(stk)
        if len(stk)==0:return ""
        else:
           return "".join(stk)

        

        