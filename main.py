# importing the random module and the string module
import random
import string

# print a welcome message
print("Hello, Welcome to Password Generator!")

# input the lenght of the password by constraining the user to type 
# numbers only
lenght = int(input("Please enter the lenght of the password -> "))

# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine the data
all = lower + upper + num + symbols

# use random 
temp = random.sample(all, lenght)

# create the password
password = "".join(temp)

# print the password
print(password)
