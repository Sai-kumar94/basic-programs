def unique_list(l):
    seen_num=[]
    for num in l:
        if num not in seen_num:
            seen_num.append(num)
    return seen_num
print(unique_list([1,2,3,4,1,2,3,4,1,2,3,4]))


# or
def unique_list(l):
    return set(l)
print(unique_list(([1,2,3,4,1,3,3,4,2,2,3,4,2])))

