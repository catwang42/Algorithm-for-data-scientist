#PROBLEM 
#14. Longest Common Prefix
"""
Input: ["flower","flow","flight"]
Output: "fl"
"""
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ''
    #find the shorest len 
    min_str_len = min([len(w) for w in strs])

    prefix = ''
    for i in range(min_str_len):
        is_prefix = strs[0][i]

        if all([word[i] == is_prefix for word in strs]):
            prefix += is_prefix
        else:
            break #if not added, will return all match case (abc, dec)-> c
    return prefix
