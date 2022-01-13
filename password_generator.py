"""""
pick a random character in uppercase, lowercase, special characters
if anyone is not in the password check if there's at least 2 of another thing and replace one with what's not there
"""
import string
import random
spec_str = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
analphabeticList = list(spec_str)


welcome = """
----------------
Welcome to the password generator app
Each password must be at least 3 characters and will contain at least one uppercase letter, one lowercase letter and one special character
----------------
"""
print(welcome)
number_of_passwords = input("How many passwords do you want to generate?: ")
while not number_of_passwords.isdigit():
    print("Must be a number")
    number_of_passwords = input("How many passwords do you want to generate?: ")
number_of_passwords = int(number_of_passwords)   

number_of_characters = input("Enter the number of characters each password should have: ")
while not number_of_characters.isdigit():
    print("Must be a number")
    number_of_characters = input("Enter the number of characters each password should have: ")
number_of_characters = int(number_of_characters)

while number_of_characters < 3 :
    print("Number of characters must be at least 3")
    number_of_characters = input("Enter the number of characters each password should have: ")
    while not number_of_characters.isdigit():
        print("Must be a number")
        number_of_characters = input("Enter the number of characters each password should have: ")
    number_of_characters = int(number_of_characters)

if number_of_passwords > 1:
    print(f"Here are your {number_of_passwords} passwords:\r\n")
else:
    print("Here is your password:\r\n")

total_list = list(string.ascii_letters) + list(analphabeticList)

for num in range(number_of_passwords):
    password = ''
    lower_list = []
    upper_list = []
    spec_list = []

    upper_check = []
    lower_check = []
    spec_check = []
    
    for number in range(number_of_characters):
        pick = random.choice(total_list)
        password += pick
    for charac in analphabeticList:
        if charac not in password:
            spec_check.append(False)
        else:
            spec_check.append(True)           
    x = any(spec_check)      
    if x == False:        
        for letter in password:
            if letter in list(string.ascii_lowercase):
                lower_list.append(letter)
        for letter in password: 
            if letter in list(string.ascii_uppercase):
                upper_list.append(letter)  
        if len(lower_list) > 1:
            password = password.replace(lower_list[0],random.choice(analphabeticList))
        elif len(upper_list) > 1:
            password = password.replace(upper_list[0],random.choice(analphabeticList))
        lower_list.clear()    
        upper_list.clear()    

    for charac in list(string.ascii_uppercase):
        if charac not in password:
            upper_check.append(False)
        else:
            upper_check.append(True)           
    x = any(upper_check)      
    if x == False:        
        for letter in password:
            if letter in list(string.ascii_lowercase):
                lower_list.append(letter)
        for letter in password: 
            if letter in analphabeticList:
                spec_list.append(letter)  
        if len(lower_list) > 1:
            password = password.replace(lower_list[0],random.choice(string.ascii_uppercase))
        elif len(spec_list) > 1:
            password = password.replace(spec_list[0],random.choice(string.ascii_uppercase))
        lower_list.clear()    
        spec_list.clear()  


    for charac in list(string.ascii_lowercase):
        if charac not in password:
            lower_check.append(False)
        else:
            lower_check.append(True)           
    x = any(lower_check)      
    if x == False:        
        for letter in password:
            if letter in list(string.ascii_uppercase):
                upper_list.append(letter)       
        for letter in password: 
            if letter in analphabeticList:
                spec_list.append(letter)         
        if len(upper_list) > 1:
            password = password.replace(upper_list[0],random.choice(string.ascii_lowercase))
        elif len(spec_list) > 1:
            password = password.replace(spec_list[0],random.choice(string.ascii_lowercase))   
        spec_list.clear()    
        upper_list.clear()  

    print(password)    
    


