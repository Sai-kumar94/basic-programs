# LIST COMPREHENSION

my_string='hello'
my_list=[x for x in my_string]
print(my_list)
#op:  ['h', 'e', 'l', 'l', 'o']

# general approach

my_string='hello'
my_list=[]
for letter in my_string:
    my_list.append(letter)
print(my_list)
# op:['h', 'e', 'l', 'l', 'o']


my_num=[num for num in range(1,10)]
print(my_num)
# op:[1, 2, 3, 4, 5, 6, 7, 8, 9]

my_num=[num**2 for num in range(1,10)]
print(my_num)
# op:[1, 4, 9, 16, 25, 36, 49, 64, 81]


my_num=[num for num in range(1,10) if num%2==0]
print(my_num)
# op:[2, 4, 6, 8]


my_num=[num for num in range(1,10) if num%2==1]
print(my_num)
# op:[1, 3, 5, 7, 9]


cel=[0,10,23,28,44]
fahrenheit=[(9/5)*temp+32 for temp in cel]
print(fahrenheit)

# [32.0, 50.0, 73.4, 82.4, 111.2]

cel=[0,10,23,28,44]
fahrenheit=[]
for temp in cel:
    fahrenheit.append((9/5)*temp+32)
print(fahrenheit)

# op:[32.0, 50.0, 73.4, 82.4, 111.2]

result=[x if x%2==0 else 'odd' for x in range(0,10)]
print(result)

# op:[0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']


nest=[]
for i in [1,2,4]:
    for j in [1,10,100]:
        nest.append(i*j)
print(nest)

# op:[1, 10, 100, 2, 20, 200, 4, 40, 400]

nest=[i*j for i in [1,2,3] for j in[1,10,100] ]
print(nest)
# [1, 10, 100, 2, 20, 200, 3, 30, 300]



