# write a python function that accepts a string and calculate the number
# of upper case letters and lower case letters

def up_low(s):
    lowercase=0
    uppercase=0
    for char in s:
        if char.isupper():
            uppercase+=1
        if char.islower():
            lowercase+=1
        else:
            pass
    print(f'original string : {s}')
    print(f'uppercase count : {uppercase}')
    print(f'lowercase count : {lowercase}  ')
up_low('Hi,How are you?')
