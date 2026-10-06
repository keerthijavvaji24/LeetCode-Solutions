class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        o=""
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        print(d)
        k=sorted(d,key=d.get,reverse=True)
        for i in k:
            o+=i*d[i]
        return o

        