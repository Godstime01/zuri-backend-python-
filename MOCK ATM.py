# mock atm
import random
print('****WELCOME TO MY MOCK ATM PROGRAM ***')

database = {} #dictionary is used as database for storing user data


def interface():
    print('***** INTERFACE ******')
    userOption = int(input('''
    Do you have an account with us? Enter 
    1 --> (yes)
    2 --> (no)
    '''))
    if userOption == 1:
        login()
    elif userOption == 2:
        register()
    else: 
        print("you have enter a wrong choice")


def register():
    firstname = input('Enter your first name')
    lastname = input('Enter last name: ')
    email = input('Enter email: ')
    username = input('enter username: ')
    password = input('Enter password: ')
    confirmPassword = input('confirm password: ')
    

def login():
    print('Login>>>>')

def generateAccountNumber():
    pass


interface()