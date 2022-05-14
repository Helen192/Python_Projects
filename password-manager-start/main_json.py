from tkinter import *
from tkinter import messagebox
import random
import pyperclip  # Using Module pyperclip to copy and paste automatically
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Using List comprehension to create a password_list
    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    # shuffle the password_list
    random.shuffle(password_list)

    #create a password which are a combination of characters in password_list
    password = "".join(password_list)
    pyperclip.copy(password)   # copy the generated password, so that user can paste it to another place

    # Insert the created password into the password field
    pass_text.insert(0, password)

    #check if user want to keep the generated password or they want to generate a new password
    is_ok = messagebox.askokcancel(title="Password", message=f"Do you want to choose {pass_text.get()} as password?")
    if is_ok:
        pass
    else:
        pass_text.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# create a file called data.json, where we will save informations of website, email and password

def save():
    website = web_text.get()
    email = email_text.get()
    password = pass_text.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }
    #If website or password fields were left empty, then a messagebox will be displayed
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            # Saving updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # clear all fields after Add button is pressed
            web_text.delete(0, END)
            pass_text.delete(0, END)

# ---------------------------- find password ------------------------------- #
# Function called find_password gets triggered when the "Search button is pressed
def find_password():
    website = web_text.get()
    # when user presses the Search button. It tries to read the data.json file
    try:
        # Read data from file data.json
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    # When data.json doesn't exist, then a messagebox is displayed
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="No Data file found")
    # When data.json exist, find the website in the data.json
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            # If website is not in the data.json, then  an error messagebox is displayed
            messagebox.showerror(title="Oops", message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

#Labels
web_label = Label(text="Website:", height=2)
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", height=2)
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:", height=2)
pass_label.grid(column=0, row=3)

#Entries
web_text = Entry(width=35)
web_text.grid(column=1, row=1, columnspan=2)
web_text.focus()

email_text = Entry(width=35)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0, "Helen@gmail.com")

pass_text = Entry(width=35)
pass_text.grid(column=1, row=3, columnspan=2)

#Buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=3, row=1)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=3, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, row=4, columnspan=2)








window.mainloop()