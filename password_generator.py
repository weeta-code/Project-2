# Author: Victor DeSouza
# Email: victordesouz@umass.edu
# SPIRE ID: 34569497
import random, string

plen = int(input('Enter a password length: '))

# def password1(password_length): # function to keep track of the length of the password
#     password_length = int(password_length)
#     return password_length

def random_int(plen):
    integer_list = [] # initializing an empty list
    for i in range(0, int(plen * .25)): # uses the value given by password1 and then taking 25% of that value as my integers
        integer_list.append(random.randint(0, 9)) # appends random numbers to the empty list according to the value given by the for loop
    return integer_list

# print (random_int()) # test

def uppercase_letters(plen):
    uppercase_list = []
    for i in range(int(plen * .25)):
        uppercase_list.append(random.choice(string.ascii_uppercase)) # appends random uppercase letters given by the value of the for loop
    return uppercase_list

# print(uppercase_letters()) # test

def lowercase_letters(plen):
    lowercase_list = []
    for i in range(int(plen * .25)):
        lowercase_list.append(random.choice(string.ascii_lowercase)) # appends random lowercase letters given by the value of the for loop
    return lowercase_list

def special_characters(plen):
    special_list = []
    for i in range(int(plen * .25)):
        special_list.append(random.choice(string.punctuation)) # appends random special characters given by the value of the for loop
    return special_list

def password_generator(plen):
    low = lowercase_letters(plen)  # First I assign all of my previous functions to local variables
    up = uppercase_letters(plen)
    num = random_int(plen)
    special = special_characters(plen)

    pass_list = low + up + num + special # I then concatenate my local variables to make one huge list
    
    pass_length = len(pass_list)
    
    if pass_length < plen:
        remaining = plen - pass_length
        for i in range(remaining):
            pass_list.append(random.choice(string.punctuation))
    
    random.shuffle(pass_list) # Shuffling the list 

    final_pass = ''.join(map(str, pass_list)) # I use the map function because when I tried type casting the list it returned with brackets and commas but map eliminated that issue
    return final_pass  # Returns the users final password
    

print(f'Here is your finalized password: {password_generator(plen)}') # My print statement declaring your password