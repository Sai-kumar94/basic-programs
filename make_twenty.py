def make_twenty(n1,n2):
    if n1+n2==20 or n1==20 or n2==20:
        return True
    else:
        return False
print(make_twenty(20,0))



# WITHOUT IF -ELSE
def make_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
print(make_twenty(2,18))