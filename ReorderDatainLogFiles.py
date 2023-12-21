# 937 leetcode

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ll=[]
        dl=[]
        for i in range(0,len(logs)):
            if ord(logs[i][-1])>57:
                ll.append(logs[i])
            else:
                dl.append(logs[i])
        print(ll)
        ll=sorted(ll,key=lambda x:x.split()[0])
        ll=sorted(ll,key=lambda x:x.split()[1:])
        print(ll)
        ll=ll+dl
        return ll