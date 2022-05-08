import json
import logging
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

from pynput.keyboard import Key, Listener
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def button_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)

    password = "".join(password_list)
   # for char in password_list:
    #    password += char

    print(f"Your password is: {password}")
    input_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def button_add():
    website = input_website.get()
    email_user = input_email_user.get()
    password = input_password.get()

    new_data = {
        website: {
            "email": email_user,
            "password": password,
        }
    }

    if len(website) == 0 or len(email_user) == 0 or len(password) == 0:
        messagebox.showerror(message="preenche tudo porra!!")
    else:
        try:
            with open("password_save.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password_save.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("password_save.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            input_email_user.delete(0, END)
            input_password.delete(0, END)


# ------------------------------SEARCH--------------------------------- #

def button_search():
    website = input_website.get()
    try:
        with open("password_save.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="erro", message="site nao encontrado")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(message=f" webiste: {website}\n user: {email}\n password: {password}",
                                title=f"{website}")
        else:
            messagebox.showinfo(message="error")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("password manager")
window.config(padx=100, pady=50)


canvas = Canvas(width=200, height=250)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=2)
label_website = Label(text="website:")
label_website.grid(column=1)
input_website = Entry(width=10)
input_website.grid(column=2)
input_website.focus()
label_email_user = Label(text="user name/email:")
label_email_user.grid(column=1)
input_email_user = Entry(width=10)
input_email_user.grid(column=2)
label_password = Label(text="Password:")
label_password.grid(column=1)
input_password = Entry(width=10)
input_password.grid(column=2)
button = Button(text="add", command=button_add)
button.grid(column=2)
button1 = Button(text="generate password", command=button_gen)
button1.grid(column=3)
button2 = Button(text="search", command=button_search)
button2.grid(column=3, row=4)
window.mainloop()
