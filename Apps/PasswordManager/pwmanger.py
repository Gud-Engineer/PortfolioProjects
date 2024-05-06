"""
Password Manager to store and generate passwords.
Not an internet based Service !! Say helloo to privacy done right !!

Salient features : Generates password, copies it to clipboard for ease of usage. Saves a local copy of the file
with all your precious credentials.
"""
import json
import secrets
import string
from tkinter import *
from tkinter import messagebox
import pyperclip


# --------------SEARCH PASSWORD---------------#
def search_password():
    search_query = website_entry.get()
    if len(search_query) == 0:
        messagebox.showinfo(title='Password Manager🏦', message='Hey! First enter an website to search!!')
    else:
        try:
            with open("data.json", "r") as datafile:
                data = json.load(datafile)

        except FileNotFoundError:
            messagebox.showwarning(title='Oops 🤭', message='Running for first time! No data in logs!')

        else:
            print(type(data))
            if search_query in data:
                search_email = data[search_query]['email']
                search_pwd = data[search_query]['password']
                select_option = messagebox.askyesnocancel(title='Search Results 📜',
                                                          message=f'Email : {search_email}\nPassword : {search_pwd}\nShall I copy the password?')
                print(select_option)
                if select_option == True:
                    messagebox.showinfo(title='Password Manager🏦', message='Hey! I have copied the password for you!!')
                    pyperclip.copy(search_pwd)
            else:
                messagebox.showwarning(title="Search Results 📜", message=f'Sorry! No Results Found for {search_query} !')
                pyperclip.copy("") # Ensuring that I don't have anything copied from previous search


# --------------PASSWORD GENERATOR---------------#
def generate_password():
    """ Generate password using newly adapted secrets' module-provides most secure source
    of randomness that OS provides.
    Default length of password is 12.
    """
    # TODO : Clean up password entry
    pwd_entry.delete(0, END)
    # TODO : Generate password using secrets module; python3.6+
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(chars) for _ in range(length))
    pwd_entry.insert(0, password)
    # TODO : Paste password using Pyperclip
    pyperclip.copy(password)  # Puts string into clipboard.


# --------------SAVE PASSWORD---------------#
def add_data():
    website = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()
    # messagebox.showinfo(title="Save 💾",message="Adding Data...")
    # TODO : Empty field checks
    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops 🤭", message="Empty Fields !!")
    else:
        # TODO : Ask user confirmation using DialogBox
        is_ok = messagebox.askokcancel(title="Save 💾", message=f"Saving password: {pwd} for site: {website}\n"
                                                               f"Ok to save?")
        # TODO : Saving data based on user confirmation
        if is_ok:
            # with open('data.txt', mode='a') as data:
            #     data.write(f'{website} | {email} | {pwd}\n')
            # TODO : JSON format data
            data_dict = {website:
                {
                    "email": email,
                    "password": pwd
                }
            }
            # TODO : Case : File exist and updating it
            try:
                # Checking if file exists, first run-> create file | next runs-> update file.
                with open('data.json', 'r') as datafile:
                    data = json.load(datafile)

            except FileNotFoundError:
                with open('data.json', 'w') as datafile:
                    json.dump(data_dict, datafile, indent=4)

            else:
                data.update(data_dict)
                with open('data.json', 'w') as datafile:
                    json.dump(data, datafile, indent=4)

            finally:
                website_entry.delete(0, END)
                pwd_entry.delete(0, END)


# --------------UI SETUP---------------#
window = Tk()
window.title('Password Manager 🔐')
window.config(padx=20, pady=20)

# TODO : Place Image
canvas = Canvas(width=250, height=250)
canvas_img = PhotoImage(file='icon.png')
canvas.create_image(125, 125, image=canvas_img)
canvas.grid(row=0, column=0, columnspan=3)

# TODO: Add Form
website_label = Label(text="Website : ")
email_label = Label(text="Email/Username : ")
pwd_Label = Label(text="Password : ")
website_label.grid(row=1, column=0, sticky="w")
email_label.grid(row=2, column=0, sticky="w")
pwd_Label.grid(row=3, column=0, sticky="w")

# TODO: Add Entry
website_entry = Entry(width=20)
email_entry = Entry(width=30)
pwd_entry = Entry(width=20)
# website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.grid(row=1, column=1, sticky="w")
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
pwd_entry.grid(row=3, column=1, sticky="w")
website_entry.focus()
email_entry.insert(0, 'xyz @gmail.com')

# TODO: Add buttons
genpwd_button = Button(text="Generate Password", command=generate_password)
savepwd_button = Button(text="Add", width=15, command=add_data)
search_button = Button(text="Search🔍", command=search_password)
genpwd_button.grid(row=3, column=2, sticky='e', padx=5)
savepwd_button.grid(row=4, column=1, columnspan=2, sticky='w')
search_button.grid(row=1, column=2, sticky='w', padx=5)
window.mainloop()
