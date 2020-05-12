import tkinter as tk
import string
import random

#Declare window height and width variables for use later
height = 500
width = 600


#Application beginning
root = tk.Tk()
root.title('Password Generator - John Cribb')
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame1 = tk.Frame(root, bg='#5B78FF')
frame1.place(relheight="1", relwidth="1")

#functions

#Gaining all the letters and numbers for generating our passwords
letters_up_and_down = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

#Generates random password based on the length specified
def password_generator(cbl, length=15):
    
    strung_together = user_choice(cbl)
    strung_together = list(strung_together)
    random.shuffle(strung_together)

    random_password = random.choices(strung_together, k=length)
    random_password = ''.join(random_password)
    return random_password

def password_combination():
  
    # convert users checkbox choices from string to boolean type
    digit_choice = eval(number_check.get().title())
    letter_choice = eval(letter_check.get().title())
    symbol_choice = eval(symbol_check.get().title())
    return [digit_choice, letter_choice, symbol_choice]

def user_choice(value):
    # converts users boolean choices into a string of the characters they have chosen 
    user_choice = ''
    user_choice += numbers if value[0] else ''
    user_choice += letters_up_and_down if value[1] else ''
    user_choice += symbols if value[2] else ''
    return user_choice

def run_generator():
    if __name__ == '__main__':
        choice_list = password_combination()
        password = password_generator(choice_list, length.get())
        passwordchoice = tk.Label(frame2, text=password)
        passwordchoice.pack()
    else:
        passwordchoice = tk.Label(frame2, text='Not run from main file, security breach.')
        passwordchoice.pack()
    
#Main Frame
frame2 = tk.Frame(frame1, bg="#eeeeee")
frame2.place(relx="0.1", rely="0.1", relheight="0.8", relwidth="0.8")

#Length Entry
password_lengths = list(range(8,33))
length = tk.IntVar()
length.set(password_lengths[7])
dropdown = tk.OptionMenu(frame2, length, *password_lengths)
dropdown.pack()

#Check Buttons
number_check = tk.StringVar()
checkbox1 = tk.Checkbutton(frame2, text='Include Numbers?', variable=number_check, onvalue='True', offvalue='False')
checkbox1.select()
checkbox1.pack()
letter_check = tk.StringVar()
checkbox2 = tk.Checkbutton(frame2, text='Include Letters?', variable=letter_check, onvalue='True', offvalue='False')
checkbox2.select()
checkbox2.pack()
symbol_check = tk.StringVar()
checkbox3 = tk.Checkbutton(frame2, text='Include Symbols?', variable=symbol_check, onvalue='True', offvalue='False')
checkbox3.select()
checkbox3.pack()

#Button
generate_button = tk.Button(frame2, text="Generate Password", command=run_generator)
generate_button.pack(side='bottom')


root.mainloop()