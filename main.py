from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
generate_button = Button(text="Generate Password", bg="#ffffff")
generate_button.grid(row=3, column=2, sticky=W)

add_button = Button(text="Add", bg="#ffffff", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



















window.mainloop()