import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import cv2
import numpy as np

# Global variable to store selected image path
fn = ""

def open_image():
    global fn

    root = tk.Tk()
    root.configure(background="white")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{w}x{h}+0+0")
    root.title("Fake Adhar Card Detection")

    # -------------- Background Image --------------
    try:
        bg_image = Image.open('s2.jpg').resize((w, h))
        background_image = ImageTk.PhotoImage(bg_image)
        background_label = tk.Label(root, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0)
    except Exception:
        root.configure(bg="white")

    # -------------- Header --------------
    label_l1 = tk.Label(
        root,
        font=("Times New Roman", 30, 'bold'),
        background="#DC143C",
        fg="white",
        width=67,
        height=2
    )
    label_l1.place(x=0, y=0)

    label_l2 = tk.Label(
        root,
        text="Fake Adhar Card Detection",
        font=("Times New Roman", 30, 'bold'),
        background="midnightblue",
        fg="white",
        width=65,
        height=2
    )
    label_l2.place(x=0, y=0)

    # -------------- Frame for Image Processing --------------
    frame_alpr = tk.LabelFrame(
        root,
        text=" Image Processing ",
        width=1000,
        height=450,
        bd=5,
        font=('times', 14, 'bold'),
        bg="black",
        fg="white"
    )
    frame_alpr.place(x=400, y=200)

    # -------------- Function: Open Image --------------
    def openimage():
        global fn
        fileName = askopenfilename(
            title='Select image for Analysis',
            filetypes=[("Image files", "*.jpg *.png *.jpeg")]
        )
        if not fileName:
            return

        fn = fileName  # store path
        IMAGE_SIZE = 200

        img = Image.open(fileName).resize((IMAGE_SIZE, 200))
        imgtk = ImageTk.PhotoImage(img)

        img_label = tk.Label(frame_alpr, image=imgtk, height=250, width=250, bg='white')
        img_label.image = imgtk
        img_label.place(x=30, y=80)

    # -------------- Function: Convert to Grey & Threshold --------------
    def convert_grey():
        global fn
        if fn == "":
            return

        IMAGE_SIZE = 200
        img = Image.open(fn).resize((IMAGE_SIZE, 200))
        img_array = np.array(img)
        x1, y1 = img_array.shape[0], img_array.shape[1]

        gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_BGR2GRAY)
        gs = cv2.resize(gs, (y1, x1))

        # Threshold
        retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Display grayscale
        im_gs = Image.fromarray(gs)
        imgtk_gs = ImageTk.PhotoImage(im_gs)
        img2 = tk.Label(frame_alpr, image=imgtk_gs, height=250, width=250, bg='white')
        img2.image = imgtk_gs
        img2.place(x=360, y=80)

        # Display thresholded
        im_th = Image.fromarray(threshold)
        imgtk_th = ImageTk.PhotoImage(im_th)
        img3 = tk.Label(frame_alpr, image=imgtk_th, height=250, width=250, bg='white')
        img3.image = imgtk_th
        img3.place(x=700, y=80)

    # -------------- Buttons --------------
    button1 = tk.Button(
        root,
        text=" Select Image ",
        command=openimage,
        width=15,
        height=1,
        font=('times', 15, 'bold'),
        bg="black",
        fg="white"
    )
    button1.place(x=50, y=300)

    button2 = tk.Button(
        root,
        text=" Image Preprocess ",
        command=convert_grey,
        width=15,
        height=1,
        font=('times', 15, 'bold'),
        bg="black",
        fg="white"
    )
    button2.place(x=50, y=450)

    root.mainloop()

# Run GUI when file is executed directly
if __name__ == "__main__":
    open_image()
