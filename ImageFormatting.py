import tkinter as tk
from tkinter import *
import cv2 as cv
import os
from tkinter import filedialog
import tkinter.messagebox
import PIL
import PIL.Image
from PIL import Image, ImageTk
from scipy.ndimage import rotate
from scipy.misc import imread, imshow

#Method to create folder at desktop
def path1():
        global mypath
        global scale
        scale = 90
        mypath = r'C:\Resized_Images'
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
        os.chdir(r'C:\Resized_Images')

def select_img():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print (root.filename)

def resize_func():
    try:
        path = root.filename
        index = path.rfind(r'/')
        append = path[index+1:]
        print(append)
        im = cv.imread(path)

        height, width = im.shape[:2]
        x = int(list1.get(ACTIVE))
        divide=100/x
        thumbnail = cv.resize(im, (int(width/divide), int(height/divide)), interpolation = cv.INTER_AREA)
        path1()
        newfilename = r'C:\Resized_Images\\new_'
        newfilename = newfilename+append

        cv.imshow(newfilename, thumbnail)
        cv.imwrite(newfilename,thumbnail)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')

def increase_scale():

    x = int(list1.get(ACTIVE))
    if x>=150:
        tkinter.messagebox.showinfo('Error','Please enter the size between 0 and 150')
    else:
        x=x+10
        y = str(x)
        list1.delete(0)
        list1.insert(0,y)

def decrease_scale():
    x = int(list1.get(ACTIVE))
    if x<=10:
        tkinter.messagebox.showinfo('Error','Please enter the size between 0 and 150')
    else:
        x=x-10
        y = str(x)
        list1.delete(0)
        list1.insert(0,y)

def pdf_convert():
    try:
        path = root.filename
        index = path.rfind(r'/')
        append = path[index+1:]

        append = append[:-4]+'.pdf'
        print(append)
        newfilename = r'C:\Resized_Images\\new_'
        newfilename = newfilename+append
        filename = path
        im = PIL.Image.open(filename)
        PIL.Image.Image.save(im, newfilename, "PDF", resoultion=70.0)
        tkinter.messagebox.showinfo('Success','PDF saved at \n C:\Resized_Images\ ')
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')

def face_detect():
    try:
        face_cascade= cv.CascadeClassifier("haarcascade_frontalface_default.xml")

        img = cv.imread("download.jpg")
        gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_img,
        scaleFactor=1.05,
        minNeighbors=5)

        for x,y,w,h in faces:
            img = cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

        print(type(faces))
        print(faces)


        cv.imshow("Gray",img)
        cv.waitKey(5000)
        path1()
        if len(str(save_as.get())):
            face_img = (str(save_as.get()))+ '.jpg'
        else:
            tkinter.messagebox.showinfo('Error','Please write Image Name First')
        cv.imwrite(face_img,img)
        cv.destroyAllWindows()
        tkinter.messagebox.showinfo('Success','Processed Image saved in \n C:\Resized_Images\ ')
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')



root = Tk()

scale = 90

b1=tk.Button(root,text="Select Image", width = 15,command=select_img)
b1.grid(row=0,column=0)


l1=Label(root,text="RESIZE AN IMAGE")
l1.grid(row=1,column=2)

b2=tk.Button(root,text="+", width = 15,command=increase_scale)
b2.grid(row=2,column=0)

list1=Listbox(root, height=1, width=10)
list1.grid(row=2,column=1)
list1.insert(0,"90")

b3=tk.Button(root,text="-", width = 15,command=decrease_scale)
b3.grid(row=2,column=2)

b4=tk.Button(root,text="Resize Image", width = 15,command=resize_func)
b4.grid(row=2,column=3)

#Image to PDF
l2=Label(root,text="IMAGE to PDF CONVERTER")
l2.grid(row=3,column=2)

b5=tk.Button(root,text="Image to PDF", width = 15,command=pdf_convert)
b5.grid(row=4,column=2)

l3=Label(root,text="DETECT FACE FROM IMAGE")
l3.grid(row=5,column=2)

l4=Label(root,text="Save file as:")
l4.grid(row=6,column=0)

global e1
save_as =StringVar()
e1=Entry(root,textvariable=save_as, width=35)
e1.grid(row=6,column=2,columnspan=15)

b6=tk.Button(root,text="DETECT FACE ", width = 15,command=face_detect)
b6.grid(row=7,column=2)


# Take a Photo From WebCam
# Image Rotate
# Detect Face from from images
root.mainloop()

"""
def rotate_90():
    try:
        path = root.filename

        index = path.rfind(r'/')
        append = path[index+1:]
        print(append)
        img = imread(path)
        path1()
        newfilename = r'C:\Resized_Images\\new_'
        newfilename = newfilename + append
        (h, w) = img.shape[:2
                    ]
# calculate the center of the image
        center = (w / 2, h / 2)

        angle90 = 90
        angle180 = 180
        angle270 = 270

        scale = 1.0

        # Perform the counter clockwise rotation holding at the center
        # 90 degrees
        M = cv.getRotationMatrix2D(center, angle90, scale)
        rotated90 = cv.warpAffine(img, M, (h, w))
        rotate_img = rotate(img, 90)
        cv.imwrite(newfilename,rotate_img)

        tkinter.messagebox.showinfo('Success','Image Rotated by 90 and Saved at \n C:\Resized_Images\ ')
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')

def rotate_180():
    try:
        path = root.filename

        index = path.rfind(r'/')
        append = path[index+1:]
        print(append)
        img = imread(path)
        path1()
        newfilename = r'C:\Resized_Images\\new_'
        newfilename = newfilename + append
        rotate_img = rotate(img, 180)
        cv.imshow(newfilename,rotate_img)
        cv.imwrite(newfilename,rotate_img)

        tkinter.messagebox.showinfo('Success','Image Rotated by 180 and Saved at \n C:\Resized_Images\ ')
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')

def rotate_270():
    try:
        path = root.filename

        index = path.rfind(r'/')
        append = path[index+1:]
        print(append)
        img = imread(path)
        path1()
        newfilename = r'C:\Resized_Images\\new_'
        newfilename = newfilename + append
        rotate_img = rotate(img, 270)
        cv.imwrite(newfilename,rotate_img)

        tkinter.messagebox.showinfo('Success','Image Rotated by 270 and Saved at \n C:\Resized_Images\ ')
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')
"""
