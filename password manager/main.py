import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letter = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    pass_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letter + pass_symbol + pass_num
    shuffle(password_list)

    full_password = "".join(password_list)
    password.insert(0, full_password)

# To copy the password to clipboard as soon as the new password is generated
    pyperclip.copy(full_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_entered = website.get()
    email_entered = username.get()
    pass_entered = password.get()

    new_data = {
        website_entered: {
            "email": email_entered,
            "password": pass_entered
        }
    }

    if len(website_entered) == 0 or len(pass_entered) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any of the fields empty!")
    else:
        try:
            #for reading and updating old data to new data
            with open("data.json", "r") as data:
                info = json.load(data)

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)

        else:
            info.update(new_data)
            #for writing or saving new data into the file
            with open("data.json", "w") as data:
                json.dump(info, data, indent=4)

        finally:
            #to clear the fields after adding the data
            website.delete(0, END)
            password.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #


def show_password():
    website_entered = website.get()
    try:
        with open("data.json", "r") as data:
            info = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if website_entered in info:
            email = info[website_entered]["email"]
            password = info[website_entered]["password"]
            messagebox.showinfo(title=f"{website_entered}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_entered} exists!")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)

label2 = Label(text="Email/Username:")
label2.grid(column=0, row=2)

label3 = Label(text="Password:")
label3.grid(column=0, row=3)

website = Entry(width=33)
website.grid(column=1, row=1)
website.focus()

username = Entry(width=52)
username.grid(column=1, row=2, columnspan=2)
username.insert(0, "your@mail_id")

password = Entry(width=33)
password.grid(column=1, row=3)

btn1 = Button(text="Generate Password", command=generate_pass, bg="#FF8B8B")
btn1.grid(column=2, row=3)

search = Button(text="Search", bg="#FF8B8B", width=15, command=show_password)
search.grid(column=2, row=1)


btn2 = Button(text="Add", width=44, command=save, bg="#EB4747", border=3)
btn2.grid(column=1, row=4, columnspan=2)


window.mainloop()
