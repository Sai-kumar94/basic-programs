mylist1=[1,2,3]
mylist2=['a','b','c']
# print(zip(mylist1,mylist2))

# output:<zip object at 0x00000257AFE9C380>

# zip function is used to zip the two lists
# together

mylist1=[1,2,3]
mylist2=['a','b','c']
for item in zip(mylist1,mylist2):
    print(item)



mylist1=[1,2,3]
mylist2=['a','b','c']
for index,item in zip(mylist1,mylist2):
    print(item)
    print(index)
    print()


mylist1=[1,2,3,4,5,6,7,8]
mylist2=['a','b','c']
for item in zip(mylist1,mylist2):
    print(item)

# zip function will zip together as afr as the list
# which is the shortest

# output:
# (1, 'a')
# (2, 'b')
# (3, 'c')








