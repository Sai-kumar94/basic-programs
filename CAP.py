
def cap(name):
    first_letter=name[0]
    fourth_letter=name[3]
    in_between=name[1:3]
    rest=name[4:]
    return first_letter.upper()+in_between+fourth_letter.upper()+rest
print(cap('thaneesh'))







