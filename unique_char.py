#Find Unique Character 
def testFun():
    assert firstUniqueChar('loveleetcode') == 2

def firstUniqChar(self, s: str) -> int:
    if not s:
        return -1
    
    h_map = {}
    for i in range(len(s)):
        if s[i] in h_map:
            h_map[s[i]] += 1
        else:
            h_map[s[i]] = 1
    
    single = [k for (k,v) in h_map.items() if v==1]
    
    return s.index(single[0]) if single !=[] else -1

import collections 

def firstUniqueChar(s:str)->int:
    char_count = collections.Counter(s)

    for k, v in enumerate(s):
        if char_count[v] ==1:
            return k 
    return -1 





