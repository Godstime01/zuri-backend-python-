'''
THIS IS A MOCK ATM 

#register - username and password, confirm password and email
#login - username or email and password
'''


# added a functionality to check acount balance and a condition to check for confirm password

import random

database = {} #dictionary

#initialize function 
def init():
    initOption = False
    print('welcome to our authentication system')
    hasAccount = int(input('''
    do you have an account with us? press
    1. (yes)
    2. (No)
    '''))
    while initOption is False:
        if hasAccount == 1:
            initOption = True
            login()
        elif(hasAccount == 2):
            initOption = True
            register()
        else:
            print("you've entered an invalid option")
    

def register():
    checkPassword = False 

    print('***********Register with us************')
    firstname = input('Enter first name: ')
    lastname = input('Enter your last name: ')
    username = input('Enter username: ')
    email = input('Enter your email address: ')
    password = input('Enter password: ')
    confirmPassword = input('Confirm password: ')


    while checkPassword is False:
        if(password != '' or confirmPassword != ''):
            if (password == confirmPassword):
                checkPassword = True
                accountNumber = generateAccountNumber()
                print('******* ACCOUNT CREATION IS SUCCESSFUL********')
                print('your account number is {accountNumber}'.format(accountNumber = accountNumber))
                database[accountNumber]=[firstname, lastname, username, email, password] #dictionary containing user details
                login()
            else:
                print('password doesn\'n match')
                register()
        else:
            print('enter password')
            continue
        # enter password again
            password = input('Enter password: ')
            confirmPassword = input('confirm password: ')

def login():
    isLoginSuccessful = False
    print('********Login*********')
    while isLoginSuccessful is False:
        print('User does not exist')
        loginUser = input('username or Email: ')
        loginpassword = input('enter password: ')

        for accountnumber, accountdetails in database.items():
            if(accountdetails[2] == loginUser or accountdetails[3] == loginUser):
                if(accountdetails[4] == loginpassword):
                    isLoginSuccessful = True
                    bankingOp()
                else:
                    print('Enter correct login details')


def bankingOp():
    global withdrawalAmount, depositAmount, accountBalance
    # initial amount when user creates an account
    accountBalance = 100 #initial account balance
    bankingOpChoice = int(input(('''
    ********BANK**********
    1. Withdrawal
    2. Deposit
    3. check acount balance 
    4. Talk with us...
    ''')))
    
    if(bankingOpChoice == 1):
        withdrawalAmount = int(input('How much do you want to withdraw: '))
        if accountBalance < 100:
            print('***Insuffient funds***')
        else:
            accountBalance -= withdrawalAmount
            anotherOp('withdrawn',1)
            
    elif(bankingOpChoice == 2):
        depositAmount = int(input('How much do you want to deposit: '))
        accountBalance += depositAmount
        anotherOp('deposited', 2)

    elif(bankingOpChoice == 3):
        print('your current acount balance is ', accountBalance)
    elif(bankingOpChoice == 4):
        print('*********TALK WITH OUR CUSTOMER CARE REPRESENTIVE***********')
    else:
        print('You enter a wrong choice!!!')


def anotherOp(operation,OpNumber):
    amount = ''
    if OpNumber == 1:
        amount = withdrawalAmount
    else:
        amount = depositAmount
        
    print(f'you\'ve successfully {operation} {amount}')
    print('''
        **************
        Would like to perform another operation

        press

        y ---> (Yes)
        n ---> (No)
        ''')

    Op = input('__---__>>> ')
    if (Op.lower() == 'y'):
        bankingOp()
    else:
        print('thanks for banking with us.')

#  generating account number function
def generateAccountNumber():
    return(random.randrange(1111111111,9999999999))

# Actual banking authentification system
init() 


