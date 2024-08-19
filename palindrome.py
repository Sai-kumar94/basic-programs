def palindrome(s):
    # remove spaces from string we are using replace
    s = s.replace(' ','')
    #check string is == reversed version of the string
    return s==s[::-1]
print(palindrome('nurses run')) 