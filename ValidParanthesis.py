class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(0,len(s)):
            if s[i]== '{' or s[i]=='[' or s[i]=='(':
                st.append(s[i])
            elif s[i]=="]" and len(st)!=0 and st[-1]=="[":
                st.pop()
            elif s[i]=="}" and len(st)!=0 and st[-1]=="{":
                st.pop()
            elif s[i]==")" and len(st)!=0 and st[-1]=="(":
                st.pop()
            else:
                return False
        if len(st)==0:
            return True
        else:
            return False