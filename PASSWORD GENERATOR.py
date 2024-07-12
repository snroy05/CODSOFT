import secrets
import random
import string

letters = string.ascii_letters
digits = string.digits
special_char = string.punctuation
selection_list = letters + digits + special_char
password_len = int(input("Enter the length of the password you want: "))
password = ' '
for i in range (password_len):
    password+= ' '.join(secrets.choice(selection_list))

print(password)
