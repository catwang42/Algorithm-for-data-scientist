#check if Reversed string?
"""
check if s = "apple" is reverse of w ="elppa"
"""
def isReserse(s:str, w:str)-> bool:
    if len(s) != len(w):
        return False
    else:
        for i, char in enumerate(s):
            if char != w[len(w)-(i+1)]:
                return False
            else:
                return True 