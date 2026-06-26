import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import cv2

##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Login")

email = tk.StringVar()
password = tk.StringVar()

# ---------- BACKGROUND ----------
image2 = Image.open('2.webp')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

#-----------------Label-------------------------
label_l1 = tk.Label(
    root,
    text="Login Form",
    font=("Times New Roman", 40, "bold"),
    bg="black",   # 
    fg="white",   # 
    bd=8,           # Border width for 3D effect
    relief="raised", # Border style
    padx=20,        # Horizontal padding
    pady=10        # Vertical padding
)
label_l1.place(x=675, y=10)


# ---------- CAMERA FUNCTION ----------
#def open_camera():
#    cap = cv2.VideoCapture(0)  # 0 = default camera
#    if not cap.isOpened():
#        ms.showerror("Error", "Camera not found")
#        return

#    while True:
#        ret, frame = cap.read()
#        if not ret:
#           break

#       cv2.imshow("Camera Feed - Press 'q' to Exit", frame)

#        if cv2.waitKey(1) & 0xFF == ord('q'):
#            break

#    cap.release()
#    cv2.destroyAllWindows()

# ---------- LOGIN FUNCTION ----------
def login():
    with sqlite3.connect('evaluation.db') as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                       "(name TEXT, address TEXT,  Email TEXT, country TEXT, Phoneno TEXT,Gender TEXT, password TEXT)")
        db.commit()

        find_entry = 'SELECT * FROM admin_registration WHERE Email = ? and password = ?'

        cursor.execute(find_entry, [(email.get()), (password.get())])
        result = cursor.fetchall()

        if result:
            ms.showinfo("Message", "Login Successfully")
            #open_camera()   #  Open camera after login
        else:
            ms.showerror('Oops!', 'Email Or Password Did Not Match.')

# ---------- REGISTRATION FUNCTION ----------
def registration():
    from subprocess import call
    call(["python", "registration.py"])
    root.destroy()

# ---------- LOGIN UI ----------
title = tk.Label(
    root, 
    text="Login Here", 
    font=("Algerian", 30, "bold", "italic"),
    bd=5, 
    bg="black",     # 
    fg="white",     # 
    relief="ridge",   # Border effect
    padx=20,          # horizontal padding
    pady=10           # vertical padding
)
title.place(x=220,y=220,width=250)
        
Login_frame=tk.Frame(root,bg="white")
Login_frame.place(x=100,y=300)
        
logolbl=tk.Label(Login_frame,bd=0).grid(row=0,columnspan=2,pady=20)
        
lbluser=tk.Label(Login_frame,text="Email",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=email,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="Green",fg="black")
btn_log.grid(row=3,column=1,pady=10)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="darkcyan",fg="black")
btn_reg.grid(row=3,column=0,pady=10)
        

root.mainloop()
