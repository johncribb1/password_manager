import tkinter as tk
from tkinter import ttk
import string
import random

PAGE_FONT = ('Roboto')
#Gaining all the letters and numbers for generating our passwords
letters_up_and_down = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

class PassHashApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, 'PassHash - Password Manager')
        
        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PasswordGenerator, PasswordVault):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    #Generates random password based on the length specified
    def password_generator(self, cbl, length=15):
        
        strung_together = self.user_choice(cbl)
        strung_together = list(strung_together)
        random.shuffle(strung_together)

        random_password = random.choices(strung_together, k=length)
        random_password = ''.join(random_password)
        return random_password

    def password_combination(self, number_check, letter_check, symbol_check):
    
        # convert users checkbox choices from string to boolean type
        digit_choice = eval(number_check.get().title())
        letter_choice = eval(letter_check.get().title())
        symbol_choice = eval(symbol_check.get().title())
        return [digit_choice, letter_choice, symbol_choice]

    def user_choice(self, value):
        # converts users boolean choices into a string of the characters they have chosen 
        user_choice = ''
        user_choice += numbers if value[0] else ''
        user_choice += letters_up_and_down if value[1] else ''
        user_choice += symbols if value[2] else ''
        return user_choice


    def run_generator(self, number_check, letter_check, symbol_check, length):
        if __name__ == '__main__':
            choice_list = self.password_combination(number_check, letter_check, symbol_check)
            password = self.password_generator(choice_list, length.get())
            passwordchoice = tk.Label(self, text='\n' + password + '\n', bg='#FFFFFF', fg='#595959', font='Roboto')
            passwordchoice.pack()
            keep_button = tk.Button(self, text="Keep Password", bg='#F8FAFF', fg='#595959', font='Roboto')
            keep_button.pack()
        
        else:
            passwordchoice = tk.Label(self, text='Not run from main file, security breach.', bg='#F8FAFF', fg='#595959', font='Roboto')
            passwordchoice.pack()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text='Welcome to PassHash\n All Your Passwords - SECURE', font=PAGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Password Generator', command=lambda: controller.show_frame(PasswordGenerator))
        button1.pack()
        button2 = ttk.Button(self, text='Password Vault', command=lambda: controller.show_frame(PasswordVault))
        button2.pack()
        button3 = ttk.Button(self, text='Nothing - Yet')
        button3.pack()


class PasswordGenerator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text='Generate a New Password', font=PAGE_FONT)
        label.pack(pady=10, padx=10)

        #Length Entry
        password_lengths = list(range(8,33))
        length = tk.IntVar()
        length.set(password_lengths[7])
        dropdown = tk.OptionMenu(self, length, *password_lengths)
        dropdown.config(activebackground='#F8FAFF', activeforeground='#595959',bg='#F8FAFF', fg='#595959', font='Roboto')
        dropdown.pack()
        
        #Check Buttons
        number_check = tk.StringVar()
        checkbox1 = tk.Checkbutton(self, text='Include Numbers?', variable=number_check, onvalue='True', offvalue='False', bg='#F8FAFF', fg='#595959', font='Roboto')
        checkbox1.select()
        checkbox1.pack()
        letter_check = tk.StringVar()
        checkbox2 = tk.Checkbutton(self, text='Include Letters?', variable=letter_check, onvalue='True', offvalue='False', bg='#F8FAFF', fg='#595959', font='Roboto')
        checkbox2.select()
        checkbox2.pack()
        symbol_check = tk.StringVar()
        checkbox3 = tk.Checkbutton(self, text='Include Symbols?', variable=symbol_check, onvalue='True', offvalue='False', bg='#F8FAFF', fg='#595959', font='Roboto')
        checkbox3.select()
        checkbox3.pack()

        #Button
        generate_button = ttk.Button(self, text="Generate Password", command=lambda: controller.run_generator(number_check, letter_check, symbol_check, length))
        generate_button.pack()

        home_button = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        home_button.pack(side='bottom')

class PasswordVault(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text='Your Password Vault', font=PAGE_FONT)
        label.pack(pady=10, padx=10)

        home_button = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        home_button.pack(side='bottom')

app = PassHashApp()
app.mainloop()