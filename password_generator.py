import string
import random

#Gaining all the letters and numbers for generating our passwords
letters_up_and_down = string.ascii_letters
numbers = string.digits
symbols = string.punctuation


#Gains the length of the password required from user
def password_length_input():
    length = input('How long do you want your password?')
    return int(length)

#Generates random password based on the length specified
def password_generator(cbl, length=15):
    
    strung_together = user_choice(cbl)
    strung_together = list(strung_together)
    random.shuffle(strung_together)

    random_password = random.choices(strung_together, k=length)
    random_password = ''.join(random_password)
    return random_password


def password_combination():
    # retrieve a user's password character combination choice
    digit_choice = input("Do you want numbers? (True or False) : ")
    letter_choice = input("Do you want letters? (True or False): ")
    symbol_choice = input("Do you want symbols? (True or False): ")

    # convert those choices from string to boolean type
    try:
        digit_choice = eval(digit_choice.title())
        letter_choice = eval(letter_choice.title())
        symbol_choice = eval(symbol_choice.title())
        return [digit_choice, letter_choice, symbol_choice]

    except NameError as e:
        print("Invalid value. Use either True or False")
        print("Invalidity returns a default, try again to regenerate")

    return [True, True, True]

    #This function returns a string of the characters which will be used to generate password based on the users choices above
def user_choice(choice_list):
        
    user_choice = ''
    user_choice += numbers if choice_list[0] else ''
    user_choice += letters_up_and_down if choice_list[1] else ''
    user_choice += symbols if choice_list[2] else ''
    return user_choice

if __name__ == '__main__':
    user_happy = 'n'
    while user_happy == 'n':
        length = password_length_input()
        choice_list = password_combination()
        password = password_generator(choice_list, length)
        print(password)
        user_happy = input('Are you happy with this one? (y or n)')
else: 
    print('Error')