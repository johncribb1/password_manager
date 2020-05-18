import os

password = 'password'
sec_key = ''


for i in password:
    ascii = ord(i) - 20
    char = chr(ascii)
    sec_key += char

#print(ascii)
#print(sec_key)

website = 'google'
login = 'pippajay1'
password = 'password'

def encrypt(website, account_login, account_password):
    # list_of_files = os.listdir()
    # if 'paulli' in list_of_files:
    #         account_file = open('paulli', 'a')
    #         get_list = account_file.read()
    #         listed = list(get_list)
    # print(listed)
    website_input = ''
    login_input = ''
    password_input = ''
    for letter in website:
        string = chr(ord(letter) - 12)
        website_input += string

    for letter in account_login:
        string = chr(ord(letter) - 12)
        login_input += string

    for letter in account_password:
        string = chr(ord(letter) - 12)
        password_input += string

    
    file = open('paulli', 'a')
    file.write(website_input + ',' + login_input + ',' + password_input + ',\n')
    file.close()


encrypt(website, login, password)
    