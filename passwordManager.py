import random
import string

#password manager
# print(website)
# print(username)
# print(password)
#input the information that we want to save
#define dictionary variable
password_list = []

def new_password():
    website =input ("Enter website?")
    username =input ("Enter username?")
    password =input ("Enter password?")
    if password == 'random':
        num_Of_digits = int(input("How many characters long should the password be ?"))
        random_password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num_Of_digits))
        print(f'This is the random password:{random_password}')
        password = random_password
    else:
        pass

    website_entry = dict([("website",website),("wusername",username),("password",password)])
    password_list.append(website_entry)
    print(password_list)


def find_password():
    looked_for_website = input('What website is it for ?')
    for entry in password_list:
        if looked_for_website == entry['website']:
            print (entry['username'])
            print (entry['password'])
            break
    print ("Website doesn't exist")


    while True:

        print('''
        Welcome to the password manager.
        Type "new" to create a new password.
        Type "show" to look up a password.
            ''')
        user_choice = input('whatcha  wanna do')
        if user_choice == 'new':
            new_password()
        elif user_choice == 'show':
           find_password()
        else:
            print("That did not compute")

    
    
