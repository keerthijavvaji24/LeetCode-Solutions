class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        l=[]
        while i<len(chars):
            ch=chars[i]
            c=0
            while i<len(chars) and ch==chars[i]:
                i+=1
                c+=1
            l.append(ch)
            if c>1:
                l.extend(str(c))
        chars[:]=l
        return len(chars)
        

        
        