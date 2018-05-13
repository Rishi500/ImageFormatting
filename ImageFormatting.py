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
        """
        index = path.rfind(r'/')
        append = path[index+1:]
        print(append)
        """
        im = cv.imread(path)

        height, width = im.shape[:2]
        x = int(list1.get(ACTIVE))
        divide=100/x
        thumbnail = cv.resize(im, (int(width/divide), int(height/divide)), interpolation = cv.INTER_AREA)
        path1()
        """newfilename = r'C:\Resized_Images\\new_'
        newfilename = newfilename+append
        """

        if len(str(save_as.get())):
            img_resize = (str(save_as.get()))+ '.jpg'
            cv.imshow(img_resize, thumbnail)
            cv.imwrite(img_resize,thumbnail)
            cv.waitKey(0)
            cv.destroyAllWindows()
            tkinter.messagebox.showinfo('Success','Image Resized and Saved at \n C:\Resized_Images\ ')
        else:
            tkinter.messagebox.showinfo('Error','Please write Image Name First')


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
        """
        index = path.rfind(r'/')
        append = path[index+1:]
        append = append[:-4]+'.pdf'
        print(append)"""

        im = PIL.Image.open(path)
        if len(str(save_as.get())):
            img_to_pdf = (str(save_as.get()))+ '.pdf'
            PIL.Image.Image.save(im, img_to_pdf, "PDF", resoultion=90.0)
            tkinter.messagebox.showinfo('Success','PDF saved at \n C:\Resized_Images\ ')
        else:
            tkinter.messagebox.showinfo('Error','Please write Image Name First')

    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')


#Face Detection Functions

def face_detect():
    try:
        face_cascade= cv.CascadeClassifier("haarcascade_frontalface_default.xml")
        path = root.filename
        img = cv.imread(path)
        gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_img,
        scaleFactor=1.05,
        minNeighbors=5)

        for x,y,w,h in faces:
            img = cv.rectangle(img,(x,y),(x+w,y+h),(100,255,10),3)


        if len(str(save_as.get())):
            face_img = (str(save_as.get()))+ '.jpg'
            path1()

            cv.imshow("Gray",img)
            cv.waitKey(4000)
            cv.imwrite(face_img,img)
            cv.destroyAllWindows()
            tkinter.messagebox.showinfo('Success','Processed Image saved in \n C:\Resized_Images\ ')
        else:
            tkinter.messagebox.showinfo('Error','Please write Image Name First')
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')
    except :
        tkinter.messagebox.showinfo('Error','An unexpected Error Occured. Run the Program Again')




#Rotate Image Functions

def rotate_90():
    try:
        path = root.filename
        path1()
        if len(str(save_as.get())):
            img_rotate_90 = (str(save_as.get()))+ '.jpg'
            img = Image.open(path)
            img2 = img.rotate(90)
            img2.save(img_rotate_90)
            tkinter.messagebox.showinfo('Success','Image Rotated by 90 and Saved at \n C:\Resized_Images\ ')

        else:
            tkinter.messagebox.showinfo('Error','Please write Image Name First')

    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')

def rotate_180():
    try:
        path = root.filename
        path1()
        if len(str(save_as.get())):
            img_rotate_180 = (str(save_as.get()))+ '.jpg'
            img = Image.open(path)
            img2 = img.rotate(180)
            img2.save(img_rotate_180)
            tkinter.messagebox.showinfo('Success','Image Rotated by 180 and Saved at \n C:\Resized_Images\ ')

        else:
            tkinter.messagebox.showinfo('Error','Please write Image Name First')
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')


def rotate_270():
    try:
        path = root.filename
        path1()
        if len(str(save_as.get())):
            img_rotate_270 = (str(save_as.get()))+ '.jpg'
            img = Image.open(path)
            img2 = img.rotate(270)
            img2.save(img_rotate_270)
            tkinter.messagebox.showinfo('Success','Image Rotated by 270 and Saved at \n C:\Resized_Images\ ')

        else:
            tkinter.messagebox.showinfo('Error','Please write Image Name First')
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')


#Take a PHOTO
def take_photo():
    try:
        cap = cv.VideoCapture(0)

        while(True):
            ret, frame = cap.read()
            rgb = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

            cv.imshow('frame', rgb)
            if cv.waitKey(1) & 0xFF == ord('q'):
                path1()
                if len(str(save_as.get())):
                    photo_webcam = (str(save_as.get()))+ '.jpg'
                    out = cv.imwrite(photo_webcam, frame)
                    break
                else:
                    tkinter.messagebox.showinfo('Error','Please write Image Name First')
                break

        cap.release()
        cv.destroyAllWindows()
        tkinter.messagebox.showinfo('Success','Photo from webcam saved.')
    except:
        tkinter.messagebox.showinfo('Error','WebCam Might be Absent.')


root = Tk()

scale = 90

b1=tk.Button(root,text="Select Image", width = 15,command=select_img)
b1.grid(row=0,column=0)


l4=Label(root,text="Save image as:")
l4.grid(row=0,column=2)

global e1
save_as =StringVar()
e1=Entry(root,textvariable=save_as, width=40)
e1.grid(row=0,column=3,columnspan=20)


l1=Label(root,text="RESIZE IMAGE")
l1.grid(row=4,column=0)

b2=tk.Button(root,text="+", width = 5,command=increase_scale)
b2.grid(row=8,column=1)

list1=Listbox(root, height=1, width=5)
list1.grid(row=8,column=2)
list1.insert(0,"  90")

b3=tk.Button(root,text="-", width = 5,command=decrease_scale)
b3.grid(row=8,column=3)

b4=tk.Button(root,text="Resize Image", width = 15,command=resize_func)
b4.grid(row=4,column=2)

#Image to PDF
l2=Label(root,text="IMAGE to PDF CONVERTER")
l2.grid(row=24,column=0)

b5=tk.Button(root,text="IMAGE TO PDF", width = 15,command=pdf_convert)
b5.grid(row=28,column=0)

l3=Label(root,text="DETECT FACE FROM IMAGE")
l3.grid(row=32,column=0)

l6=Label(root,text="TAKE A PHOTO")
l6.grid(row=32,column=3)

l7=Label(root,text="COMPRESS IMAGE")
l7.grid(row=24,column=3)

b6=tk.Button(root,text="DETECT FACE ", width = 15,command=face_detect)
b6.grid(row=36,column=0)

b6=tk.Button(root,text="COMPRESS IMAGE ", width = 15,command=face_detect)
b6.grid(row=28,column=3)

l5=Label(root,text="ROTATE IMAGE")
l5.grid(row=16,column=2)

b7=tk.Button(root,text="ROTATE 90 DEG ", width = 15,command=rotate_90)
b7.grid(row=16,column=1)

b8=tk.Button(root,text="ROTATE 180 DEG ", width = 15,command=rotate_180)
b8.grid(row=16,column=3)

b9=tk.Button(root,text="ROTATE 270 DEG ", width = 15,command=rotate_270)
b9.grid(row=20,column=2)

b10=tk.Button(root,text="TAKE A PHOTO (Press Q)", width = 30,command=take_photo)
b10.grid(row=36,column=3)

# Take a Photo From WebCam
# Image Rotate
# Detect Face from from images
root.mainloop()
