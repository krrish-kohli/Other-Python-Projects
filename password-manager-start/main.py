from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) > 0 and len(email) > 0 and len(password) > 0:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Creating json file
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(END, "dummy_email@gmail.com")
            password_entry.delete(0, END)

    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email_value = data[website]["email"]
            password_value = data[website]["password"]
            messagebox.showinfo(title="Details", message=f"Email/Username: {email_value} \nPassword: {password_value}")
        else:
            messagebox.showinfo(title="Error", message="No details for the {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #


# Setting up the window.
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Adding the logo.
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Writing the text website.
website = Label(text="Website:")
website.grid(column=0, row=1)

# Adding the text entry for website.
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

# Adding the search button.
search = Button(text="Search", width=12, command=find_password)
search.grid(column=2, row=1)

# Writing the text Email/Username.
email = Label(text="Email/Username:")
email.grid(column=0, row=2)

# Adding the text entry for email.
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "dummy_email@gmail.com")

# Writing the text Password.
password = Label(text="Password:")
password.grid(column=0, row=3)

# Adding the text entry for password.
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Adding the generate password button.
generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(column=2, row=3)

# Adding the add button.
add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
