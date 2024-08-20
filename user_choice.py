def user_choice():
    choice='WRONG'
    while choice.isdigit()==False:
        choice=input('enter a number between (0-10): ')
    return int(choice)
print(user_choice())

# output:
# enter a number between (0-10): fwnwn
# enter a number between (0-10): winfow
# enter a number between (0-10): sonfwof
# enter a number between (0-10): jfnw
# enter a number between (0-10): 4
# 4
