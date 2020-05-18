import tkinter as tk
from tkinter import ttk
import bcrypt
import os
import string
import random

app_color = '#ffffff'
PAGE_FONT = ('Roboto')
#Gaining all the letters and numbers for generating our passwords
letters_up_and_down = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

logged_in_name = ' '

class PassHashApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, 'PassHash - Password Manager')


        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, RegisterPage, StartPage, PasswordGenerator, SetPassPage, PasswordVault):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(LoginPage)

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


    def run_generator(self, number_check, letter_check, symbol_check, length, password_text):
        if __name__ == '__main__':
            choice_list = self.password_combination(number_check, letter_check, symbol_check)
            
            
            password_text.set(self.password_generator(choice_list, length.get()))
            
            
        else:
            passwordchoice = tk.Label(self, text='Not run from main file, security breach.', bg=app_color, font=PAGE_FONT)
            passwordchoice.pack()

    def reg_user(self, username, password, user_entry, pass_entry):
        username_info = username.get().encode('UTF-8')
        password_info = password.get().encode('UTF-8')
        
        hashed = bcrypt.hashpw(password_info, bcrypt.gensalt())

        file = open(username_info, 'wb')
        #file.write(username_info)
        file.write(hashed)
        #file.write(password_info)
        file.close()

        user_entry.delete(0, 100)
        pass_entry.delete(0, 100)

        success_label = tk.Label(self, text='Registration Success')
        success_label.pack()

    def login_verify(self, username, password, user_entry, pass_entry,user_message):
        username_info = username.get()
        password_info = password.get().encode('UTF-8')

        user_entry.delete(0, 100)
        pass_entry.delete(0, 100)

        list_of_files = os.listdir()
        if username_info in list_of_files:
            file1 = open(username_info, 'rb')
            verify = file1.read()
            #verify = file1.read().splitlines()
            #if password_info in verify:
            if bcrypt.checkpw(password_info, verify):
                global logged_in_name
                logged_in_name = username_info
                self.show_frame(StartPage)
            else:
                user_message.set('Password Not Recognised')
        else:
            user_message.set('User Not Found')



class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg=app_color)

        label = tk.Label(self, text='Register Page', font=PAGE_FONT, bg=app_color)
        label.pack(pady=20, padx=20)

        username = tk.StringVar()
        password = tk.StringVar()

        user_label = tk.Label(self, text='Username', bg=app_color)
        user_label.pack()
        user_entry = ttk.Entry(self, textvariable=username)
        user_entry.pack()
        pass_label = tk.Label(self, text='Password', bg=app_color)
        pass_label.pack()
        pass_entry = ttk.Entry(self, textvariable=password)
        pass_entry.pack(pady=10)

        reg_button = ttk.Button(self, text='Register', command=lambda: controller.reg_user(username, password, user_entry, pass_entry))
        reg_button.pack()
        back_button = ttk.Button(self, text='Back To Login', command=lambda: controller.show_frame(LoginPage))
        back_button.pack(side='bottom', pady=10)

        

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg=app_color)

        label = tk.Label(self, text='Welcome to PassHash\n All Your Passwords \n SECURE', font=PAGE_FONT, bg=app_color)
        label.pack(pady=20, padx=20)

        label = tk.Label(self, text='Please enter your login details below', bg=app_color)
        label.pack()

        username = tk.StringVar()
        password = tk.StringVar()

        user_label = tk.Label(self, text='Username', bg=app_color)
        user_label.pack()
        user_entry = ttk.Entry(self, textvariable=username)
        user_entry.pack()
        pass_label = tk.Label(self, text='Password', bg=app_color)
        pass_label.pack()
        pass_entry = ttk.Entry(self, textvariable=password)
        pass_entry.pack(pady=10)

        button1 = ttk.Button(self, text='Login', command=lambda: controller.login_verify(username, password, user_entry, pass_entry, user_message))
        button1.pack(pady=10, padx=20)
        button2 = ttk.Button(self, text='Register', command=lambda: controller.show_frame(RegisterPage))       
        button2.pack(pady=10, padx=20)
        
        user_message = tk.StringVar()
        message_holder = tk.Label(self, textvariable=user_message, bg=app_color)
        message_holder.pack(side='bottom')

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg=app_color)

        logged_in_message = 'Signed in as ' + logged_in_name

        label = tk.Label(self, text='Welcome to PassHash\n All Your Passwords - SECURE', font=PAGE_FONT, bg=app_color)
        label.pack(pady=20, padx=20)
        labe2 = tk.Label(self, text=logged_in_message, font=PAGE_FONT, bg=app_color)
        labe2.pack(pady=20, padx=20)

        button1 = ttk.Button(self, text='Password Generator', command=lambda: controller.show_frame(PasswordGenerator))
        button1.pack(pady=10, padx=20)
        button2 = ttk.Button(self, text='Password Vault', command=lambda: controller.show_frame(PasswordVault))
        button2.pack(pady=10, padx=20)
        button3 = ttk.Button(self, text='Nothing - Yet')
        button3.pack(pady=10, padx=20)


class PasswordGenerator(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg=app_color)

        label = tk.Label(self, text='Generate a New Password', font=PAGE_FONT, bg=app_color)
        label.pack(pady=10, padx=10)

        #Length Entry
        password_lengths = list(range(8,33))
        length = tk.IntVar()
        length.set(password_lengths[7])
        dropdown = tk.OptionMenu(self, length, *password_lengths)
        dropdown.config(activebackground='#F8FAFF', activeforeground='#595959',bg=app_color, fg='#595959', font='Roboto')
        dropdown.pack()
        
        #Check Buttons
        number_check = tk.StringVar()
        checkbox1 = tk.Checkbutton(self, text='Include Numbers?', variable=number_check, onvalue='True', offvalue='False', bg=app_color, fg='#595959', font='Roboto')
        checkbox1.select()
        checkbox1.pack()
        letter_check = tk.StringVar()
        checkbox2 = tk.Checkbutton(self, text='Include Letters?', variable=letter_check, onvalue='True', offvalue='False', bg=app_color, fg='#595959', font='Roboto')
        checkbox2.select()
        checkbox2.pack()
        symbol_check = tk.StringVar()
        checkbox3 = tk.Checkbutton(self, text='Include Symbols?', variable=symbol_check, onvalue='True', offvalue='False', bg=app_color, fg='#595959', font='Roboto')
        checkbox3.select()
        checkbox3.pack()

        password_text = tk.StringVar()
        password_text.set('Click Generate Below')
        pass_holder = tk.Label(self, textvariable=password_text, bg=app_color, fg='#595959', font='Roboto')
        pass_holder.pack(padx=10, pady=10)

        keep_button = ttk.Button(self, text="Keep Password", command=lambda: controller.show_frame(SetPassPage))
        keep_button.pack()

        #Button
        generate_button = ttk.Button(self, text="Generate Password", command=lambda: controller.run_generator(number_check, letter_check, symbol_check, length, password_text))
        generate_button.pack()

        home_button = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        home_button.pack(side='bottom', pady=(0,10))

class PasswordVault(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg=app_color)

        label = tk.Label(self, text='Your Password Vault', font=PAGE_FONT)
        label.pack(pady=10, padx=10)

        home_button = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        home_button.pack(side='bottom')


class SetPassPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg=app_color)

        label = tk.Label(self, text='Your Password Vault', font=PAGE_FONT)
        label.pack(pady=10, padx=10)

        home_button = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        home_button.pack(side='bottom')

app = PassHashApp()
app.geometry('252x448')
app.mainloop()