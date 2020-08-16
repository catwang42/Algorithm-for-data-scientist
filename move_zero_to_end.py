#PROBLEM 
def testMoveZeros():
    nums = [0,0,1,0,2,0,3,4]
    assert moveZeroes(nums)==[1,2,3,2,0,0,0],"Function Failed"
    

def moveZeroes( nums: List[int]) -> None:
    first_zero = None 
    for i , val in enumerate(nums):
        if val == 0 and first_zero is None:
            first_zero = i 
            #print('find fist zero index', i)
        if val != 0 and first_zero is not None:
            #print('swape number {} with zero at index {}'.format(nums[i],first_zero))
            nums[i] , nums[first_zero] =  nums[first_zero], nums[i]
            first_zero += 1 
            #print('change first zero index' ,first_zero)

