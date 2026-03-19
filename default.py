from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# ---------------- LOGIN FUNCTION ----------------
def login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "asish@gmail.com" and password == "1234":
        messagebox.showinfo("Login Status", "Hala Madrid! Login Successful ⚽")
    else:
        messagebox.showerror("Login Status", "Invalid Email or Password")


# ---------------- MAIN WINDOW ----------------
root = Tk()
root.title("Real Madrid Login")
root.iconbitmap("rmf.ico")
root.geometry("520x560")
root.configure(bg="#0a1f44")   # deep navy blue


# ---------------- CARD FRAME ----------------
card = Frame(root, bg="white")
card.place(relx=0.5, rely=0.5, anchor=CENTER, width=380, height=520)  # 🔥 fixed height


# ---------------- IMAGE (LOGO) ----------------
img = Image.open("rmf.png")   # replace with Real Madrid logo if you have
img = img.resize((90, 90))
img = ImageTk.PhotoImage(img)

img_label = Label(card, image=img, bg="white")
img_label.pack(pady=(25,10))


# ---------------- TITLE ----------------
title = Label(card,
              text="REAL MADRID",
              font=("Segoe UI",18,"bold"),
              bg="white",
              fg="#0a1f44")
title.pack()

subtitle = Label(card,
                 text="Member Login",
                 font=("Segoe UI",10),
                 bg="white",
                 fg="grey")
subtitle.pack(pady=(0,15))


# ---------------- EMAIL ----------------
email_label = Label(card,
                    text="Email",
                    font=("Segoe UI",10,"bold"),
                    bg="white",
                    fg="#0a1f44")
email_label.pack(anchor="w", padx=40)

email_entry = Entry(card,
                    font=("Segoe UI",11),
                    bg="#f5f5f5",
                    fg="black",
                    bd=1,
                    relief="solid",
                    width=28)
email_entry.pack(padx=40, pady=(5,15), ipady=6)


# ---------------- PASSWORD ----------------
password_label = Label(card,
                       text="Password",
                       font=("Segoe UI",10,"bold"),
                       bg="white",
                       fg="#0a1f44")
password_label.pack(anchor="w", padx=40)

password_entry = Entry(card,
                       font=("Segoe UI",11),
                       bg="#f5f5f5",
                       fg="black",
                       bd=1,
                       relief="solid",
                       show="*",
                       width=28)
password_entry.pack(padx=40, pady=(5,20), ipady=6)


# ---------------- LOGIN BUTTON ----------------
login_btn = Button(card,
                   text="LOGIN",
                   font=("Segoe UI",11,"bold"),
                   bg="#0a1f44",
                   fg="white",
                   activebackground="#163d7a",
                   activeforeground="white",
                   bd=0,
                   padx=30,
                   pady=10,
                   command=login)
login_btn.pack(pady=10)


# ---------------- FOOTER ----------------
footer = Label(card,
               text="© Real Madrid Fan UI",
               font=("Segoe UI",8),
               bg="white",
               fg="grey")
footer.pack(side="bottom", pady=10)


# ---------------- ENTER KEY LOGIN ----------------
root.bind('<Return>', lambda event: login())

root.mainloop()