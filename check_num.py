# write a function that checks whether a number is in a given range(inclusive of high an dlow)

def check_rand_num(num,low,high):
    return num in range(low,high+1)
print(check_rand_num(5,2,7))
print(check_rand_num(1,3,5))

# or

def check_rand_num(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range of {low} and {high}')
    else:
        print('not in range')
print(check_rand_num(2,4,56))
print(check_rand_num(5,2,7))