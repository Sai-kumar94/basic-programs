# LIST COMPREHENSION
num_str="2 3 5 7 8 0"
list_str=num_str.split()
list_str= [int(num) for num in list_str]
print(list_str)

# USING FOR LOOP:
num_str="2 3 5 7 8 0"
list_str=num_str.split()
int_list=[]
for num in list_str:
    int_list.append(int(num))
print(int_list)