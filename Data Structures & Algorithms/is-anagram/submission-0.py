class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_feq = {}
        t_feq = {}

        for i in range(len(s)):
            s_feq[s[i]] = s_feq.get(s[i],0) + 1
            t_feq[t[i]] = t_feq.get(t[i],0) + 1
        
        for k, v in s_feq.items():
            if t_feq.get(k, 0) != v:
                return False

        return True