user_input = 'random'
data = []

def menu() :
    print('''   <<< THE MENU >>>
1/ Add An Ithem
2/ Mark As Done
3/ Show To Do Ithem
4/ EXIT
5/ Show the menu''')
menu()
while user_input != '4' :
    user_input = input('Enter Your Choise : ')
    
    if user_input == '1':
        ithem = input('What is to be done ? ').lower()
        data.append(ithem)
        print('added ithem ',ithem)

    elif user_input == '2':
        ithem = input( 'What is to be marked as done ? ').lower()
        if ithem in data :
            data.remove(ithem)
            print( 'You are removed : ',ithem)
        else :
            print("Ithem does not exist")     

    elif user_input == '3':
        print ('>>>LIST OF TO DO ITHEM<<<')
        for ithem in data :
            print(ithem)

    elif user_input == '4':
        print('GoodBye') 

    elif user_input == '5':
        menu()

    else :
        print('Please Can you enter 1 , 2 , 3 or 4')  