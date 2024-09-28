# Author: Victor DeSouza
# Email: victordesouz@umass.edu
# SPIRE ID: 34569497
import random, string

plen = int(input('Enter a password length: '))

def password1(password_length): # function to keep track of the length of the password
    password_length = int(password_length)
    return password_length

def random_int():
    integer_list = [] # initializing an empty list
    for i in range(0, int(password1(plen) * .25)): # uses the value given by password1 and then taking 25% of that value as my integers
        integer_list.append(random.randint(0, 9)) # appends random numbers to the empty list according to the value given by the for loop
    return integer_list

# print (random_int()) # test

def uppercase_letters():
    uppercase_list = []
    for i in range(int(password1(plen) * .25)):
        uppercase_list.append(random.choice(string.ascii_uppercase)) # appends random uppercase letters given by the value of the for loop
    return uppercase_list

# print(uppercase_letters()) # test

def lowercase_letters():
    lowercase_list = []
    for i in range(int(password1(plen) * .25)):
        lowercase_list.append(random.choice(string.ascii_lowercase)) # appends random lowercase letters given by the value of the for loop
    return lowercase_list

def special_characters():
    special_list = []
    for i in range(int(password1(plen) * .25)):
        special_list.append(random.choice(string.punctuation)) # appends random special characters given by the value of the for loop
    return special_list

def password_generator():
    low = lowercase_letters()  # First I assign all of my previous functions to local variables
    up = uppercase_letters()
    num = random_int()
    special = special_characters()

    pass_list = low + up + num + special # I then concatenate my local variables to make one huge list
    random.shuffle(pass_list) # Shuffling the list 

    final_pass = ''.join(map(str, pass_list)) # I use the map function because when I tried type casting the list it returned with brackets and commas but map eliminated that issue
    return final_pass  # Returns the users final password
    

print(f'Here is your finalized password: {password_generator()}') # My print statement declaring your password