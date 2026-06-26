import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import *


# Create the main application window
root = tk.Tk()
root.configure(background="whitesmoke")
root.title("Main")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

image2=Image.open('1.png')
image2=image2.resize((w,h),Image.LANCZOS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)


def reg():
    from subprocess import call
    call(["python","registration.py"])
    
    
def log():
    from subprocess import call
    call(["python","login.py"])

#################################################################################   
    
canvas = tk.Canvas(root, bg="#000000", highlightthickness=0)
canvas.place(x=0, y=0, width=w, height=70)
text_var = " Audio based Disease Detection "
text = canvas.create_text(
    w,
    35,
    text=text_var,
    font=('Times New Roman', 28, 'bold'),
    fill='white',
    tags=("marquee",),
    anchor='w'
)

fps = 40

def shift():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    if x2 < 0:
        canvas.coords("marquee", w, 35)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000 // fps, shift)

shift()

#####################################################################################
#canvas0 = tk.Canvas(root,background="black",height=2,width=1700,borderwidth=0, highlightthickness=0)
#canvas0.place(x=2,y=15)

#canvas0 = tk.Canvas(root,background="black",height=2,width=1700,borderwidth=0, highlightthickness=0)
#canvas0.place(x=2,y=80)


#Create a horizontal line by drawing a line on the Canvas
#line0 = canvas0.create_line(380, 20, 380, 120, fill="white", width=1)

# label = tk.Label(root, text='''PERSONALITY''' ,background="white",font=("Times New Roman",35))
# label.place(x=100,y=500)


# label01=tk.Label(root,text="CENTER",background="white",font=("Times New Roman",15),)
# label01.place(x=170,y=550)


              
              
# button2= tk.Button(root, text='''ABOUT US''' ,background="white",font=("Times New Roman",30),bd=0,command=about)
# button2.place(x=1000,y=500)


# image_paths =[
#               "f.jpg",
#               # "202108-Sliders-06Corrections.png",
#               # "202108-Sliders-05AttorneysInvestigative.png",
#               # "202108-Sliders-03Government.png",
#               # "202108-Sliders-02Poilice.png",
#               # "202108-Sliders-01EyeDetect-branding.png"
#               ]

# image_label = tk.Label(root, height=500, width=1500,background="white")
# image_label.place(x=0,y=150)

# Index to keep track of the current image
current_image_index = 0

button1= tk.Button(root, text='''REGISTER''',background="white" ,font=("Times New Roman",30),bd=0,command=reg )
button1.place(x=770,y=700)

button4= tk.Button(root, text="LOG IN" ,background="white",font=("Times New Roman",30),bd=0,command=log)
button4.place(x=550,y=700)

# update_image()
root.mainloop()