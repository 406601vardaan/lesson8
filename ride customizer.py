print('Select your nide:')
print('1.Bike')
print('2.Car')

choice= int(input('Enter your choice:'))

if(choice==1):
    print('What type of bike?')
    print('Scooty\n')
    print('Scooter\n')

    choice2=int(input('Enter your choice2:'))
    if choice2==1:
        print('you have selected scooty')
    else:
        print('You have selected scooter')
elif(choice==2):
    print('Seden')
    print('XUV')
    choice3=int(input('enter your choice3:'))
    if choice3==1:
        print('You have selected sedan')
    else:
        print('you hvae selected XUV')
else:
    print('Wrong choice!')