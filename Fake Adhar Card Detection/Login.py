import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import cv2

##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("700x700+200+100")
root.title("Login Form")




username = tk.StringVar()
password = tk.StringVar()
        

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('5.jpg')
image2 = image2.resize((w,h), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


#######################################################################################
#  Title of the page #
# -------- Marquee Header Canvas --------
header_width = 1550  # adjust to match your window width
header_height = 70

header_canvas = tk.Canvas(root, bg="black", highlightthickness=0)  
header_canvas.place(x=0, y=0, width=header_width, height=header_height)

marquee_text = " Fake Adhar Card Detection "
text_id = header_canvas.create_text(
    header_width, header_height // 2,
    text=marquee_text,
    font=("Times New Roman", 40, "bold"),
    fill='white',
    tags="marquee",
    anchor='w'
)

fps = 40        # frames per second
shift_speed = 2 # pixels per frame

def shift_text():
    x1, y1, x2, y2 = header_canvas.bbox("marquee")
    if x2 < 0:
        header_canvas.coords("marquee", header_width, header_height // 2)
    else:
        header_canvas.move("marquee", -shift_speed, 0)
    header_canvas.after(int(1000 / fps), shift_text)

shift_text()

################################################################################



def registration():
    from subprocess import call
    call(["python","Registration.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("Message", "LogIn Sucessfull")
            # ===========================================
            root.destroy()
            
            from subprocess import call
            call(["python","GUI_Master.py"])

            

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')


# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

# label_l2 = tk.Label(root, text="___ Login Form ___",font=("Times New Roman", 30, 'bold'),
#                     background="#EEEE00", fg="black", width=67, height=3)
# label_l2.place(x=0, y=90)


# bg1_icon=ImageTk.PhotoImage(file="D:\\module\30 % code\\30 % code\\b2.png")

# bg_icon=ImageTk.PhotoImage(file="D:\\module\\30 % code\\30 % code\\L.jpg")
# user_icon=ImageTk.PhotoImage(file="D:\\module\\30 % code\\30 % code\\l1.png")
# pass_icon=ImageTk.PhotoImage(file="D:\\module\\30 % code\\30 % code\\p1.jpg")
        
# bg_lbl=tk.Label(root,image=bg1_icon, width=600,height=600)
# bg_lbl.place(x=50,y=50)
        

# ------------------ Main Title ------------------
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
        
lbluser=tk.Label(Login_frame,text="Username",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
txtuser=tk.Entry(Login_frame,bd=5,textvariable=username,font=("",15))
txtuser.grid(row=1,column=1,padx=20)
        
lblpass=tk.Label(Login_frame,text="Password",compound=LEFT,font=("Times new roman", 20, "bold"),bg="white").grid(row=2,column=0,padx=50,pady=10)
txtpass=tk.Entry(Login_frame,bd=5,textvariable=password,show="*",font=("",15))
txtpass.grid(row=2,column=1,padx=20)
        
btn_log=tk.Button(Login_frame,text="Login",command=login,width=15,font=("Times new roman", 14, "bold"),bg="Green",fg="black")
btn_log.grid(row=3,column=1,pady=10)
btn_reg=tk.Button(Login_frame,text="Create Account",command=registration,width=15,font=("Times new roman", 14, "bold"),bg="darkcyan",fg="black")
btn_reg.grid(row=3,column=0,pady=10)
        
        
    

root.mainloop()