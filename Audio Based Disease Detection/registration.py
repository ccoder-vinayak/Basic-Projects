import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os
import cv2



window = tk.Tk()
window.geometry("900x1500")
window.title("REGISTRATION FORM")
window.configure(background="black")

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()
policeno = tk.IntVar()
value = random.randint(1, 1000)
print(value)

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM admin_registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO admin_registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.askquestion("askquestion", "Are you sure?")
            ms.askokcancel("askokcancel", "Want to continue?")
            ms.showinfo('Success!', 'Account Created Successfully !')
            from subprocess import call
            call(["python", "Login.py"])
        
            # window.destroy()
            #window.destroy() 

#####################################################################################################################################################
def login():
     from subprocess import call
     call(["python", "Login.py"])
     window.destroy()
 
    
#def register():
 #    from subprocess import call
  #   call(["python", "lecture_login.py"])



# assign and define variable
# def login():

    
#####For background Image
image2 = Image.open('6.webp')
image2 = image2.resize((1531, 790), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

title_font = ("Helvetica", 36, "bold")

# -------- Marquee Header Canvas --------
header_width = 1550  # adjust to match your window width
header_height = 70

header_canvas = tk.Canvas(window, bg="#000000", highlightthickness=0)
header_canvas.place(x=0, y=0, width=header_width, height=header_height)

marquee_text = "  Registration Form  "
text_id = header_canvas.create_text(
    header_width, header_height // 2,
    text=marquee_text,
    font=('Times New Roman', 28, 'bold'),
    fill='white',
    tags="marquee",
    anchor='w'
)

fps = 40  # speed control (higher = smoother)
shift_speed = 2  # pixels per frame

def shift_text():
    x1, y1, x2, y2 = header_canvas.bbox("marquee")
    if x2 < 0:
        header_canvas.coords("marquee", header_width, header_height // 2)
    else:
        header_canvas.move("marquee", -shift_speed, 0)
    header_canvas.after(int(1000 / fps), shift_text)

shift_text()


bg_frame = tk.Frame(window, bg="#f0f0f0", bd=5, relief="ridge")
bg_frame.place(x=530, y=140, width=500, height=450)  # adjust to cover all labels & entries

# ------------------ Labels and Entries (keep your positions) ------------------
l2 = tk.Label(window, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="#f0f0f0")
l2.place(x=550, y=150)
t1 = tk.Entry(window, textvariable=Fullname, width=20, font=('', 15))
t1.place(x=750, y=150)

l3 = tk.Label(window, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="#f0f0f0")
l3.place(x=550, y=200)
t2 = tk.Entry(window, textvariable=address, width=20, font=('', 15))
t2.place(x=750, y=200)

l5 = tk.Label(window, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="#f0f0f0")
l5.place(x=550, y=250)
t4 = tk.Entry(window, textvariable=Email, width=20, font=('', 15))
t4.place(x=750, y=250)

l6 = tk.Label(window, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="#f0f0f0")
l6.place(x=550, y=300)
t5 = tk.Entry(window, textvariable=Phoneno, width=20, font=('', 15))
t5.place(x=750, y=300)

l7 = tk.Label(window, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="#f0f0f0")
l7.place(x=550, y=350)
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="#f0f0f0", font=("bold", 15), variable=var, value=1).place(x=750, y=350)
tk.Radiobutton(window, text="Female", padx=20, width=4, bg="#f0f0f0", font=("bold", 15), variable=var, value=2).place(x=850, y=350)

l8 = tk.Label(window, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="#f0f0f0")
l8.place(x=550, y=400)
t6 = tk.Entry(window, textvariable=age, width=20, font=('', 15))
t6.place(x=750, y=400)

l4 = tk.Label(window, text="User Name :", width=12, font=("Times new roman", 15, "bold"), bg="#f0f0f0")
l4.place(x=550, y=450)
t3 = tk.Entry(window, textvariable=username, width=20, font=('', 15))
t3.place(x=750, y=450)

l9 = tk.Label(window, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="#f0f0f0")
l9.place(x=550, y=500)
t9 = tk.Entry(window, textvariable=password, width=20, font=('', 15), show="*")
t9.place(x=750, y=500)

l10 = tk.Label(window, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"), bg="#f0f0f0")
l10.place(x=550, y=550)
t10 = tk.Entry(window, textvariable=password1, width=20, font=('', 15), show="*")
t10.place(x=750, y=550)

#REGISTER BUTTON#
btn = tk.Button(window, text="Register", bg="black",font=("",20),fg="white", width=9, height=0, command = insert)
btn.place(x=700,y=600)

window.mainloop()