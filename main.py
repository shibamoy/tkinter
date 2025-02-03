from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_maker():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
    ranlet = [random.choice(letters) for _ in range(8)]
    rannum = [random.choice(numbers) for _ in range(4)]
    ransym = [random.choice(symbols) for _ in range(2)]
    password_list = ranlet + ransym + rannum
    random.shuffle(password_list)
    new_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    account = f"{website} | {email} : {password}"

    # confirm = messagebox.askyesno(title="Confirm creation", message=f"Are you sure you want to add account for {website}: \n"
    #                                                       f"{email}:{password} ?")
    if len(website) < 1 or len(password) < 1:
        error = messagebox.showerror(title="Ooops", message="Please fill out website/password")

    # confirm = messagebox.askyesno(title="Confirm creation",
    #                               message=f"Are you sure you want to add account for {website}: \n"
    #                                       f"{email}:{password} ?")

    else:
        confirm = messagebox.askyesno(title="Confirm creation",
                        message=f"Are you sure you want to add account for {website}: \n"
                                f"{email}:{password} ?")
        if confirm:
            with open("data.txt", "a") as file:
                file.write(account + "\n")
            website_entry.delete(0, END)
            # email_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

# Create the main window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2,sticky='w')
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2,sticky='w')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1,sticky='w')

# Buttons
generate_password_button = Button(text="Generate Password", command=password_maker)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()