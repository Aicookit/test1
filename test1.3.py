import random
computer=random.randrange(1,100)
print('please enter any number in 1-100:')
for i in range(1,9):
    you=int(input())
    if you>computer:
        print('it is too big')
    elif you<computer:
        print('it is too small' )
    else:
        break
    if you!=computer:
        print("sorry,it's not the number!please enter again:")
    else:
        print('yes,you are right,the anwser is:'+str(computer))




