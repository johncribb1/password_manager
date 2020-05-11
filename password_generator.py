import string
import random

#Gaining all the letters and numbers for generating our passwords
letters_up_and_down = string.ascii_letters
numbers = string.digits
symbols = string.punctuation


#Gains the length of the password required from user
def password_length():
    length = input('How long do you want your password?')
    return int(length)

#Generates random password based on the length specified
def password_generator(length=15):
    
    strung_together = f'{letters_up_and_down}{numbers}{symbols}'
    strung_together = list(strung_together)
    random.shuffle(strung_together)

    random_password = random.choices(strung_together, k=length)
    random_password = ''.join(random_password)
    return random_password

print(password_generator(25))