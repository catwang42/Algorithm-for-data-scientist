#Add two number  
# 123 + 286 
def addStrings1(num1, num2):
    i , j = len(num1)-1 , len(num2) -1
    pass_next = 0 
    result = ''

    temp1 , temp2 = 0, 0 
    
    while i >= 0 or j >= 0:
        temp1 = int(num1[i]) if i >= 0 else 0 
        temp2 = int(num2[j]) if j >= 0 else 0 
        
        result += str((pass_next + temp1 + temp2)%10)
        pass_next = (pass_next + temp1 + temp2)//10
        
        i -= 1 
        j -= 1 

    if pass_next>0:
        result += str(pass_next)
    return result[::-1]