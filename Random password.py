import random

#User input for password length 
passlen = int(input("Enter the length of password: "))

#storing letters, numbers and special characters
all_char="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

#random sampling by joining the length of the password and the variable all_char
passw = "".join(random.sample(all_char,passlen ))
print(passw)