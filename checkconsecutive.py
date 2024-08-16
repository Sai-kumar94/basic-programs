def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    else:
        return False
print(has_33([1,2,3,4,4,5,5,3,3]))

# here we have to use for else block . we cannot write if-else because for loop iterates every time
# and checks if condition.



# or we can also do this with slicing

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i:i+2]==[3,3]:
            return True
    else:
        return False
print(has_33([1,2,3,4,4,5,5,3,3]))










