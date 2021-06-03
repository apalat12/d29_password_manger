from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json


# --------------------create password ------------------------#
def generate_password():
    password_entry.delete(0, 'end')
    Uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Upper_word = "".join([random.choice(Uppercase) for _ in range(3)])
    Lowercase = Uppercase.lower()
    Lower_word = "".join([random.choice(Lowercase) for _ in range(5)])
    Special_char = "! @ # $ % ^ & * ( ) { } [ ] / + = ~"
    Special_word = "".join([random.choice(Special_char.split(" ")) for _ in range(5)])
    Numbers = "1,2,3,4,5,6,7,8,9"
    Number_word = "".join([random.choice(Numbers.split(",")) for _ in range(5)])
    rand_str = Upper_word + Lower_word + Special_word + Number_word
    lst = list(rand_str)
    # print(lst)
    random.shuffle(lst)
    # print(lst)
    password_entry.insert(0, "".join(lst))
    pyperclip.copy("".join(lst))


# ----------------- saving the data to a file -----------------#
def save_data():
    # print(web_var.get(),email_var.get(),pass_var.get())
    website = web_var.get().title()
    email = email_var.get()
    password = pass_var.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        usr = messagebox.askokcancel(title=website,
                                     message=f"Details to be saved: \nEmail:{email}\nPassword:{password}\nIs it OK to save?")
        if usr:
            try:
                with open("data.json", 'r') as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("data.json", 'w') as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open("data.json", 'w') as file:
                    json.dump(new_data, file, indent=4)

            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()


# ----------------- Reading the data to a file -----------------#
def read_data():
    website = web_var.get().title()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
        try:
            e = data[website]["email"]
            p = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {e}\nPassword: {p}")
            website_entry.delete(0,'end')
        except KeyError:
            messagebox.showinfo(title="Error", message="website not found")

    except FileNotFoundError:
        messagebox.showinfo(title="No Database",message="File not found")


# ------------------------UI Setup --------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

web_var = StringVar()
website_entry = Entry(width=36, textvar=web_var)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_var = StringVar()
email_entry = Entry(width=36, textvar=email_var)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "abhijeetpalatkar12@gmail.com")

pass_var = StringVar()
password_entry = Entry(width=36, textvar=pass_var)
password_entry.grid(row=3, column=1)

button1 = Button(text="Generate Password", command=generate_password)
button1.grid(row=3, column=3)
add_button = Button(text="Add", width=31, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=14, command=read_data)
search.grid(row=1, column=3)

window.mainloop()
