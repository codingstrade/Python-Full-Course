import random
import string

def generate_password(length, strength):
    lowercase = string.ascii_lowercase # all letters from a-z in lowercase
    uppercase = string.ascii_uppercase # all letters from A-Z in Uppercase
    digits = string.digits # return all numbers
    punctuation = string.punctuation # / $ ! etc

    if strength == 'weak':
        chars = lowercase
    elif strength == 'medium':
        chars = lowercase + digits
    else:
        chars = lowercase + uppercase + digits + punctuation

    password = ''.join(random.choice(chars) for _ in range(length) )
    return password

while True:
    try:
        length = int(input("Enter the length of the password: "))
        break
    except ValueError:
        print("Please Enter a valid Integer.")
while True:
    strength = input("Enter The strength of the password (weak, medium or Strong): ")
    if strength in ['weak', 'medium', 'strong']:
        break
    else:
        print("Please enter a valid strength listed in the Text!")

password = generate_password(length, strength)

print("Your password is: ", password)
