from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_maker():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [[random.choice(numbers) for char in range(nr_numbers)],
                     [random.choice(symbols) for char in range(nr_symbols)],
                     [random.choice(letters) for char in range(nr_letters)]]
    new_pass_list = [char for sublist in password_list for char in sublist]
    random.shuffle(password_list)

    password = ""
    for char in new_pass_list:
        password += char
    password_input.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def data_add():
    new_dict = {
        website_input.get(): {
            'email': login_input.get(),
            'password': password_input.get()
        }
    }
    length = {'website': website_input.get(), 'login': login_input.get(), 'password': password_input.get()}
    length_2 = {website_input.get(): 'website', login_input.get(): 'login', password_input.get(): 'password'}
    for symbol in length.values():
        if len(symbol) == 0:
            return messagebox.showwarning(title=f'Wrong {length_2[symbol]}.', message=f'You need to name {length_2[symbol]} first.')
    question = messagebox.askokcancel(title=website_input.get(),
                                      message=f'These are the details entered:\nLogin:{login_input.get()}'
                                              f'\nPassword:{password_input.get()}\nIs it okay to save?')
    if question == True:
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
                data.update(new_dict)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        except:
            with open('data.json', 'w') as file:
                json.dump(new_dict, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

def search():
    wanted_website = website_input.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title='Error', message='Information not found.')
    else:
        for website in data.keys():
            if wanted_website == website:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=wanted_website, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showwarning(title='Error', message='Information not found.')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=50)


canvas = Canvas(window, width=200, height=200)
canvas.grid(row=0, column=1)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)

website_label = Label(text='Website: ')
website_label.grid(row=1, column=0)
website_input = Entry()
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky='ew')

login_label = Label(text='Email/Username: ')
login_label.grid(row=2,column=0)
login_input = Entry()
login_input.insert(END, 'valeriy.kraffchenko@gmail.com')
login_input.grid(row=2, column=1, columnspan=2, sticky='ew')

password_label = Label(text='Password: ', highlightthickness=0)
password_label.grid(row=3, column=0)
password_input = Entry()
password_input.grid(row=3, column=1, sticky='ew')

generate_button = Button(text='Generate Password', highlightthickness=0, command=password_maker)
generate_button.grid(row=3, column=2, sticky='ew')

add_button = Button(text='Add', command=data_add)
add_button.grid(row=4, column=1, columnspan=2, sticky='ew')

search_button = Button(text='Search', command=search)
search_button.grid(row=1, column=2, sticky='ew')






window.mainloop()