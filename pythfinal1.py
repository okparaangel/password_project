import random
import string
import secrets

print ("PasswordManager") 

#     def __init__(self):
#         self.password = {}
#         self.password_dict = {}
#         self = passwordManager ()
#         self= masterPassword ()

users = [
    {"username": "Amby", "email": "amby@gmail.com", "password": "password1"},
    {"username": "Eva", "email": "eva@gmail.com", "password": "password2"},
    {"username": "Ebus", "email": "ebus@gmail.com", "password": "password3"}
]

admin = [
    {'user': 'admin_1', 'password': 'R3work_@c@d3my1'},
    {'user': 'admin_2', 'password': 'R3work_@c@d3my2'}
]



print('Register')
first_name = input('enter your first name: ') 
last_name = input('enter your last name: ') 
user_name = input('enter your username: ') 
email = input('enter your email address: ')
 
def generate_password():
    symbols = "@#$"
    letters = string.ascii_letters + string.digits
    password = ''.join(random.choice(letters) for i in range(10))
    password += random.choice(symbols)  # Add a random symbol
    password += ''.join(random.choice(letters) for i in range(1))  # Add a random character
    password = ''.join(random.sample(password, len(password)))  # Shuffle the password
    return password


while True:
    pass_word = input("Do you want a random password? (yes/no): ").lower()
    if pass_word == 'yes':
        random_password = generate_password()
        print("Random Password: ", random_password)
        break
    elif pass_word == 'no':
        password = input("Enter password: ")
        if len(password) < 8: 
            print("Password must not be less than 8 characters.")
        elif not any(char.isupper() for char in password): 
            print('Password must contain at least one uppercase letter.')
        elif not any(char.islower() for char in password):
            print('Password must contain at least one lowercase letter.')
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least one number.")
        else:
            print('Password is okay.')
            break
    else:
        print("Please enter 'yes' or 'no'.")
    


with open("user_info.txt", "a") as file:
    file.write(f"firs tname: {first_name}\n")
    file.write(f"last name: {last_name}\n")
    file.write(f"Username: {user_name}\n")
    file.write(f"Email: {email}\n")
    if pass_word == 'yes':
        file.write(f"Random Password: {random_password}\n")
    else:
        file.write("User opted not to generate a random password.\n")
        file.write(f"Chosen Password: {password}\n")

print('Do you want to view user info? [YES or NO]: ')
while True:
    user_info_choice = input("(yes/no): ").lower()

    if user_info_choice == 'yes':
        # Assume you have the admin list as in the previous examples
        admin = [
            {'user': 'admin_1', 'password': 'R3work_@c@d3my1'},
            {'user': 'admin_2', 'password': 'R3work_@c@d3my2'}
        ]

        def authenticate(username, password):
            for user_info in admin:
                if user_info['user'] == username and user_info['password'] == password:
                    return True
            return False

        username = input("Enter AdminUsername: ")
        password = input("Enter MasterPassword: ")
        if authenticate(username, password):
            with open('user_info.txt', 'r') as file:
                for line in file:
                    print(line.strip())
        else:
            print("Authentication failed. Please check your username and password.")
    elif user_info_choice == 'no':
        break
    else:
        break


# Input credentials
username = input("Enter AdminUsername: ")
password = input("Enter MasterPassword: ")

if authenticate(username, password):
    with open('user_info.txt', 'r') as file:
        for line in file:
            print(line.strip())
else:
    print("Authentication failed. Please check your username and password.")
