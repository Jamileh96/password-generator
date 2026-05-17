import tkinter
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for letter in range(nr_letters)]
    symbol_list = [random.choice(symbols) for symbol in range(nr_symbols)]
    number_list = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def click_add():
    website = website_entry.get().title()
    email = email_entry.get().title()
    password = password_entry.get().title()
    new_data = {website: {
        "email": email,
        "password": password
    }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        empty = messagebox.showwarning(title="Warning", message="You have not entered any details")
    else:
        okay = messagebox.askokcancel(title=website, message=f"These are  the detailed entered: \nEmail: {email} \nPassword: {password}"
                                                  f"\nIs it okay to save?")
        if okay:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                # If the file isn't there, then create a new file with the data in it
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # If the file WAS found, we update the existing dictionary
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                # No matter what happened above, delete out our previous entry
                website_entry.delete(0, "end")
                email_entry.delete(0, "end")
                password_entry.delete(0, "end")

# ---------------------------- SEARCH DATA ------------------------------- #
def find_data():
    website = website_entry.get().title()
    email = email_entry.get().title()
    password = password_entry.get().title()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="the data you entered do not exist")
    else:
        if website in data:
            user_email = data[website]["email"]
            user_password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {user_email}"
                                                       f"\n Password: {user_password}")
        else:
            messagebox.showwarning(title="Warning", message= f"No data for {website} found")




# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas( width=200, height=200, highlightthickness=0)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/User Name")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password")
password_label.grid(row=3, column=0)

website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

Generate_pass = tkinter.Button(text="Generate Password", width=20, command=generate_password)
Generate_pass.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width = 36, command=click_add)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = tkinter.Button(text="Search", width=20, command=find_data)
search_button.grid(row=1, column=2)

















window.mainloop()