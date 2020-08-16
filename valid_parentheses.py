################################
#MAP
#Problem 
#check Valid Parentheses
def testFun():
    assert isValid("{[]}") is True, "Funtion failed, should be True"
    assert isValid("{[]") is False, "Funtion failed, should be False"

def isValid(s:str)->bool:
    deque=[s[0]]
    mapping = {'(': ')', '{': '}', '[' : ']'}
    n = len(s)
    
    for i in range(1,n):
        if deque[-1] in mapping and mapping[deque[-1]] == s[i]:
            deque.pop()
        else:
            deque.append(s[i])
    return deque == []
