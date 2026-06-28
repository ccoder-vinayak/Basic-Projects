#from distutils.command.upload import upload
from tkinter.tix import IMAGE
from django.contrib import messages
from django.shortcuts import  render, redirect

from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, logout, authenticate #add this
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import cv2
import numpy as np
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from tensorflow.keras.applications import vgg16
from tensorflow.keras.models import load_model
import base64
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image , ImageTk 
from tensorflow.keras.optimizers import Adam

#from keras.optimizers import Adam
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.python.keras.backend import set_session
global up
up=""

def index(request):
	return render(request, 'index.html')
def classification(request):
	return render(request, 'classification.html')

def classification(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fn=upload
        print("uploaded:",fn)
        
    
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        print("save ", file)
        file_url = fss.url(file)
        print("url:",file_url)       
        IMAGE_SIZE = 64
        LEARN_RATE = 1.0e-4
        CH=3
        print(fn)
        print(type(fn))
        
        #img = cv2.imread('C:/new/21C9588-Rice prediction/rice_web/rice_web/media/image.png',0)
        img = Image.open(fn)
        img = np.array(img.convert('L'))
		
        
        #img = cv2.imread(a,0)
                
            #rnjn
            #load in greyscale mode
        print(img)
		
        filename1 = 'media/grey.jpeg'
        cv2.imwrite(filename1, img)
		
       
        file_url1 = fss.url(filename1)
        print("url:",file_url1) 
        # file1 = fss.save(img.name, img)
        # print("save ", file1)
        # file_url1 = fss.url(file1)
        # print("url:",file_url1)  
       
        #convert into binary
        ret,binary = cv2.threshold(img,160,255,cv2.THRESH_BINARY)# 160 - threshold, 255 - value to assign, THRESH_BINARY_INV - Inverse binary
        #img.save('media/binary.jpeg')
        filename2 = 'media/binary.jpeg'
		
        cv2.imwrite(filename2, binary)
		
        return render(request, "classification.html", {'file_url': file_url})  

    else:
    
        return render(request, "classification.html") #
    #return render(request, "classification.html")


def index(request):        
        return render(request, "index.html")

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('/login1/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login1(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('index')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login1')