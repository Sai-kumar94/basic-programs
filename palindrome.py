def palindrome(s):
    # remove spaces from string we are using replace
    s = s.replace(' ','')
    #check string is == reversed version of the string
    return s==s[::-1]
print(palindrome('nurses run'))


def is_palindrome(string):
    string=string.lower()
    return string==string[::-1]
print(is_palindrome("madam"))


def is_palindrome(string):
    if string==string[::-1]:
        print('it is a palindrome')
    else:
        print('not a palindrome')
print((is_palindrome("madam")))