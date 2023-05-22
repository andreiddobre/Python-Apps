#pip install random
import random

#user input for password length 
pass_length = int(input("Enter the length of password: "))

#storing letters, numbers and special characters
all_char = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

#random sampling by joining the length of the password and the variable all_char
generated_pass = "".join(random.sample(all_char, pass_length))

#print generated_pass
print(generated_pass)
