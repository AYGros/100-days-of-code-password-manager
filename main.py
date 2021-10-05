from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    #pw_list = [random.choice(letters)]

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = symbols_list + letters_list + numbers_list
    random.shuffle(password_list)

    my_password = "".join(password_list)
    password_input.insert(0, my_password)
    pyperclip.copy(my_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = user_input.get()
    password = password_input.get()

    if not website or not password:
        alert = messagebox.showwarning(title="Missing Info", message="Please fill in all fields")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n"
                                                      f"Password: {password} \nIs it ok to save?")

        if is_ok:
            with open("passwords.txt", "a") as passwords_file:
                passwords_file.write(f"{website}  |  {email}  |  {password}\n")
            website_input.delete(0, END)
            user_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#ffffff")

canvas = Canvas(width=200, height=200, bg="#ffffff", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:", bg="#ffffff")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:", bg="#ffffff")
user_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="#ffffff")
password_label.grid(row=3, column=0)

#entries
website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()


user_input = Entry(width=40)
user_input.grid(row=2, column=1, columnspan=2)
user_input.insert(0, "AYGros@email.de")

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

#buttons
generate_button = Button(text="Generate Password", bg="#ffffff", command=generate_password)
generate_button.grid(row=3, column=2, sticky=W)

add_button = Button(text="Add", bg="#ffffff", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



















window.mainloop()