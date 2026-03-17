from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# ---------------- LOGIN FUNCTION ----------------
def login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "asish@gmail.com" and password == "1234":
        messagebox.showinfo("Login Status", "Login Successful")
    else:
        messagebox.showerror("Login Status", "Invalid Email or Password")


# ---------------- MAIN WINDOW ----------------
root = Tk()  
root.title("Student Login")
root.iconbitmap("pixel2.ico")
root.geometry("500x520")
root.configure(bg="#121212")


# ---------------- CARD FRAME ----------------
card = Frame(root, bg="#1e1e1e")
card.place(relx=0.5, rely=0.5, anchor=CENTER, width=360, height=430)


# ---------------- IMAGE ----------------
img = Image.open("star.png")
img = img.resize((80, 70))
img = ImageTk.PhotoImage(img)

img_label = Label(card, image=img, bg="#1e1e1e")
img_label.pack(pady=(20,5))


# ---------------- TITLE ----------------
title = Label(card,
              text="ASISH BUCKS",
              font=("Segoe UI",18,"bold"),
              bg="#1e1e1e",
              fg="#00c896")
title.pack(pady=5)


# ---------------- EMAIL ----------------
email_label = Label(card,
                    text="Email",
                    font=("Segoe UI",11),
                    bg="#1e1e1e",
                    fg="#cccccc")
email_label.pack(anchor="w", padx=40, pady=(20,3))

email_entry = Entry(card,
                    font=("Segoe UI",11),
                    bg="#2a2a2a",
                    fg="white",
                    insertbackground="white",
                    bd=0,
                    width=28)
email_entry.pack(padx=40, ipady=7)


# ---------------- PASSWORD ----------------
password_label = Label(card,
                       text="Password",
                       font=("Segoe UI",11),
                       bg="#1e1e1e",
                       fg="#cccccc")
password_label.pack(anchor="w", padx=40, pady=(15,3))

password_entry = Entry(card,
                       font=("Segoe UI",11),
                       bg="#2a2a2a",
                       fg="white",
                       insertbackground="white",
                       bd=0,
                       show="*",
                       width=28)
password_entry.pack(padx=40, ipady=7)


# ---------------- LOGIN BUTTON ----------------
login_btn = Button(card,
                   text="Login",
                   font=("Segoe UI",12,"bold"),
                   bg="#00c896",
                   fg="black",
                   activebackground="#00a87c",
                   activeforeground="black",
                   bd=0,
                   padx=25,
                   pady=8,
                   command=login)
login_btn.pack(pady=30)


# ---------------- ENTER KEY LOGIN ----------------
root.bind('<Return>', lambda event: login())

root.mainloop()