#PROBLEM 
#maxium remve one char and be palindrome 
def testPalindrome():
    assert validPalindrome('asbcba') is True , "Function error"

def validPalindrome(s: str) -> bool:
    start, end = 0, len(s)-1
    while start<end:
        if s[start] != s[end]:
            left = s[start+1:end+1]
            right = s[start:end]
            return left == left[::-1] or right == right[::-1]
            #print('left', left)
            #rint('right',right)
        start += 1 
        end -= 1
     
    return True