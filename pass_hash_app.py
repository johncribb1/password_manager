import tkinter as tk
from tkinter import ttk
import bcrypt
import os
import string
import random

app_color = '#dbedff'
banner_color = '#0060c7'
PAGE_FONT = ('Roboto', 12)
PAGE_FONT2 = ('Roboto', 10)
entry_box_size = 25

#Gaining all the letters and numbers for generating our passwords
letters_up_and_down = string.ascii_letters
numbers = string.digits
symbols = string.punctuation


class PassHashApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, 'PassHash - Password Manager')


        self.logged_in = tk.StringVar()

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, RegisterPage, StartPage, PasswordGenerator, KeepPassPage, PasswordVault, AddLoginPage):

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

    def reg_user(self, username, password, user_entry, pass_entry, register_message):
        username_info = username.get().encode('UTF-8')
        password_info = password.get().encode('UTF-8')
        
        hashed = bcrypt.hashpw(password_info, bcrypt.gensalt())

        file = open(username_info, 'wb')
        file.write(hashed)
        file.close()
        file2 = open(username.get() + 'li', 'w')
        file2.close()

        user_entry.delete(0, 100)
        pass_entry.delete(0, 100)

        register_message.set('Registration Success')

    def login_verify(self, username, password, user_entry, pass_entry, user_message):
        username_info = username.get()
        password_info = password.get().encode('UTF-8')

        user_entry.delete(0, 100)
        pass_entry.delete(0, 100)

        list_of_files = os.listdir()
        if username_info in list_of_files:
            file1 = open(username_info, 'rb')
            verify = file1.read()    
            if bcrypt.checkpw(password_info, verify):
                self.logged_in.set(str(username_info))
                self.show_frame(StartPage)

            else:
                user_message.set('Password Not Recognised')
        else:
            user_message.set('User Not Found')

    def readfile(self, frame):
        file_to_open = self.logged_in.get() + 'li'
        f = open(file_to_open, 'r')
        count = 0

        for line in f:
            entityList = line.split(',')
            
            website = entityList[0]
            login = entityList[1]
            password = entityList[2]

            website_decrypt = ''
            login_decrypt = ''
            password_decrypt = ''

            for letter in website:
                string = chr(ord(letter) + 12)
                website_decrypt += string

            for letter in login:
                string = chr(ord(letter) + 12)
                login_decrypt += string

            for letter in password:
                string = chr(ord(letter) + 12)
                password_decrypt += string

            website_col = tk.Label(frame, text=website_decrypt, font=PAGE_FONT, bg=app_color) 
            website_col.grid(row=2 + count, sticky='w')
            login_col = tk.Label(frame, text=login_decrypt, font=PAGE_FONT, bg=app_color) 
            login_col.grid(row=2 + count, column=1)
            password_col = tk.Label(frame, text=password_decrypt, font=PAGE_FONT, bg=app_color)
            password_col.grid(row=2 + count, column=2, sticky='e')
            count += 1
        f.close()

    def add_entry(self, *args):
        website_info = args[0].get()
        login_info = args[1].get()
        password_info = args[2].get()

        website_encrypt = ''
        login_encrypt = ''
        password_encrypt = ''

        for letter in website_info:
            string = chr(ord(letter) - 12)
            website_encrypt += string

        for letter in login_info:
            string = chr(ord(letter) - 12)
            login_encrypt += string

        for letter in password_info:
            string = chr(ord(letter) - 12)
            password_encrypt += string
    
        file_to_open = self.logged_in.get() + 'li'
        file = open(file_to_open, 'a')
        file.write(website_encrypt + ',' + login_encrypt + ',' + password_encrypt + ',\n')
        file.close()

        args[3].delete(0, 100)
        args[4].delete(0, 100)
        args[5].delete(0, 100)




class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg=app_color)

        label = tk.Label(self, text='Register Page', font=PAGE_FONT, bg=app_color)
        label.pack(pady=20, padx=20)

        username = tk.StringVar()
        password = tk.StringVar()

        user_label = tk.Label(self, text='Username', font=PAGE_FONT2, bg=app_color)
        user_label.pack()
        user_entry = ttk.Entry(self, textvariable=username)
        user_entry.pack(pady=10)
        pass_label = tk.Label(self, text='Password', font=PAGE_FONT2, bg=app_color)
        pass_label.pack()
        pass_entry = ttk.Entry(self, textvariable=password)
        pass_entry.pack(pady=10)

        reg_button = ttk.Button(self, text='Register', command=lambda: controller.reg_user(username, password, user_entry, pass_entry, register_message))
        reg_button.pack(pady=(10,10))

        logo = tk.PhotoImage(file='images/lock3.png')
        lock_label = tk.Label(self, image=logo, width=100, height=100, bg=app_color)
        lock_label.photo = logo
        lock_label.pack()

        back_button = ttk.Button(self, text='Back To Login', command=lambda: controller.show_frame(LoginPage))
        back_button.pack(side='bottom', pady=10)

        register_message = tk.StringVar()
        success_label = tk.Label(self, textvariable=register_message, font=PAGE_FONT2, bg=app_color)
        success_label.pack()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg=app_color)
        banner = tk.Frame(self, bg=banner_color)
        banner.pack(side='top', fill='x')

        label = tk.Label(banner, text='Welcome to PassHash\n All Your Passwords \n SECURE', font=PAGE_FONT, bg=banner_color)
        label.pack()

        label = tk.Label(self, text='Please enter your login details below:', font=PAGE_FONT2, bg=app_color)
        label.pack()

        username = tk.StringVar()
        password = tk.StringVar()

        user_label = tk.Label(self, text='Username', font=PAGE_FONT2, bg=app_color)
        user_label.pack(pady=(10,0))
        user_entry = ttk.Entry(self, textvariable=username, width=entry_box_size)
        user_entry.pack()
        pass_label = tk.Label(self, text='Password', bg=app_color, font=PAGE_FONT2)
        pass_label.pack()
        pass_entry = ttk.Entry(self, textvariable=password, show="*", width=entry_box_size)
        pass_entry.pack(pady=(0,10))

        
        logo = tk.PhotoImage(file='images/lock3.png')
        lock_label = tk.Label(self, image=logo, width=100, height=100, bg=app_color)
        lock_label.photo = logo
        lock_label.pack()
        

        button1 = ttk.Button(self, text='Login', command=lambda: controller.login_verify(username, password, user_entry, pass_entry, user_message))
        button1.pack(pady=10, padx=20)
        button2 = ttk.Button(self, text='Register', command=lambda: controller.show_frame(RegisterPage))       
        button2.pack(pady=10, padx=20)
        
        user_message = tk.StringVar()
        message_holder = tk.Label(self, textvariable=user_message, font=PAGE_FONT, bg=app_color)
        message_holder.pack(side='bottom')

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg=app_color)
        

        label = tk.Label(self, text='Welcome to PassHash\n Signed in as:', font=PAGE_FONT, bg=app_color)
        label.pack(pady=10, padx=10)
        
        logged_in_label = tk.Label(self, textvariable=controller.logged_in, bg=app_color)
        logged_in_label.pack()        

        button1 = ttk.Button(self, text='Password Generator', command=lambda: controller.show_frame(PasswordGenerator))
        button1.pack(pady=10, padx=20)
        button2 = ttk.Button(self, text='Password Vault', command=lambda: controller.show_frame(PasswordVault))
        button2.pack(pady=10, padx=20)
        button3 = ttk.Button(self, text='Add Login', command=lambda: controller.show_frame(AddLoginPage))
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

        keep_button = ttk.Button(self, text="Keep Password", command=lambda: controller.show_frame(KeepPassPage))
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
        
        label = tk.Label(self, text='Your Password Vault', font=PAGE_FONT, bg=app_color)
        label.pack(pady=10, padx=10)
        frame1 = tk.Frame(self, height=350, width=200, bg=app_color)
        frame1.pack()
        entity_label = tk.Label(frame1, text='Your Passwords', font=PAGE_FONT, bg=app_color)
        entity_label.grid(columnspan=3, row=0)
        website_label = tk.Label(frame1, text='Website: ', font=PAGE_FONT, bg=app_color)
        login_label = tk.Label(frame1, text='Login: ', font=PAGE_FONT, bg=app_color)
        password_label = tk.Label(frame1, text='Password: ', font=PAGE_FONT, bg=app_color)
        website_label.grid(row=1)
        login_label.grid(row=1, column=1)
        password_label.grid(row=1, column=2)

        home_button = tk.Button(self, text='Go Home', command=lambda: controller.show_frame(StartPage))
        home_button.pack(side='bottom', pady=10)
        add_button = ttk.Button(self, text='Add a Login', command=lambda: controller.show_frame(AddLoginPage))
        add_button.pack(side='bottom', pady=10)
        obtain_button = ttk.Button(self, text='Obtain Passcodes', command=lambda: controller.readfile(frame1))
        obtain_button.pack(side='bottom', pady=10)
        
class KeepPassPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg=app_color)

        label = tk.Label(self, text='Your Password Vault', font=PAGE_FONT)
        label.pack(pady=10, padx=10)

        home_button = ttk.Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        home_button.pack(side='bottom')

class AddLoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg=app_color)

        label = tk.Label(self, text='Register Page', font=PAGE_FONT, bg=app_color)
        label.pack(pady=20, padx=20)

        website = tk.StringVar()
        login = tk.StringVar()
        password = tk.StringVar()


        website_label = tk.Label(self, text='Website:', bg=app_color)
        website_label.pack()
        website_entry = ttk.Entry(self, textvariable=website)
        website_entry.pack()
        login_label = tk.Label(self, text='Login', bg=app_color)
        login_label.pack()
        login_entry = ttk.Entry(self, textvariable=login)
        login_entry.pack(pady=10)
        password_label = tk.Label(self, text='Password', bg=app_color)
        password_label.pack()
        password_entry = ttk.Entry(self, textvariable=password)
        password_entry.pack(pady=10)

        add_button = ttk.Button(self, text='Add Login', command=lambda: controller.add_entry(website, login, password, website_entry, login_entry, password_entry))
        add_button.pack()
        back_button = ttk.Button(self, text='Back Home', command=lambda: controller.show_frame(StartPage))
        back_button.pack(side='bottom', pady=10)


app = PassHashApp()
app.geometry('252x448')
app.mainloop()