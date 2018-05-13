import tkinter as tk
from tkinter import *
import cv2 as cv
import os
from tkinter import filedialog
import tkinter.messagebox
import PIL
import PIL.Image
from PIL import Image, ImageTk
from tkinter import ttk

#Method to create folder at desktop
def path1():
        global mypath
        global scale
        scale = 90
        mypath = r'C:\IMAGE_FORMATTING_APP'
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
        os.chdir(r'C:\IMAGE_FORMATTING_APP')

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
            tkinter.messagebox.showinfo('Success','Image Resized and Saved at \n C:\IMAGE_FORMATTING_APP ')
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
            tkinter.messagebox.showinfo('Success','PDF saved at \n C:\IMAGE_FORMATTING_APP ')
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
            tkinter.messagebox.showinfo('Success','Processed Image saved in \n C:\IMAGE_FORMATTING_APP ')
        else:
            tkinter.messagebox.showinfo('Error','Please write Image Name First')
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')
    except :
        tkinter.messagebox.showinfo('Error','An unexpected Error Occured Run the Program Again')




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
            tkinter.messagebox.showinfo('Success','Image Rotated by 180 and Saved at \n C:\IMAGE_FORMATTING_APP ')

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
            tkinter.messagebox.showinfo('Success','Image Rotated by 270 and Saved at \n C:\IMAGE_FORMATTING_APP ')

        else:
            tkinter.messagebox.showinfo('Error','Please write Image Name First')
    except AttributeError:
        tkinter.messagebox.showinfo('Error','Please select an Image First')


#Take a PHOTO
def take_photo():
    try:
        if len(str(save_as.get())):
            cap = cv.VideoCapture(0)

            while(True):
                ret, frame = cap.read()
                rgb = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

                cv.imshow('Press Q to SAVE IMAGE', rgb)
                if cv.waitKey(1) & 0xFF == ord('q'):
                    path1()

                    photo_webcam = (str(save_as.get()))+ '.jpg'
                    out = cv.imwrite(photo_webcam, frame)
                    break


            cap.release()
            cv.destroyAllWindows()
            tkinter.messagebox.showinfo('Success','Photo from webcam saved.')
        else:
            tkinter.messagebox.showinfo('Error','Please write Image Name First')


    except:
        tkinter.messagebox.showinfo('Error','WebCam Might be Absent.')


root = Tk()
root.title("Image Formatting Application - Win 64(Bit)")
root.configure(bg="#e8f5e9")


scale = 90

b1=ttk.Button(root,text="Select Image", width = 15,command=select_img)
b1.grid(row=0,column=0,padx=4,pady=4)


l4=Label(root,text="Save file as:",fg='#303F9F',bg='#c8e6c9',font='Calibri 11 bold')
l4.grid(row=1,column=0,padx=4,pady=0)

break1=Label(root,text="____________________________________________________________________________________________",fg='#303F9F',bg="#e8f5e9",font='Calibri 11 bold')
break1.grid(row=2,column=0,padx=4,pady=1,columnspan=7)


global e1
save_as =StringVar()
e1=Entry(root,textvariable=save_as, width=35)
e1.grid(row=1,column=2,columnspan=3,padx=4,pady=4)



l1=Label(root,text="RESIZE AN IMAGE",fg='#303F9F',bg='#c8e6c9',font='Calibri 11 bold')
l1.grid(row=3,column=2,columnspan=3,pady=4,padx=7)

b2=ttk.Button(root,text="-", width = 15,command=decrease_scale)
b2.grid(row=4,column=2,padx=4)

list1=Listbox(root, height=1, width=5,font='Calibri 11 bold')
list1.grid(row=4,column=3,padx=4)

list1.insert(0,"90")

b3=ttk.Button(root,text="+", width = 15,command=increase_scale)
b3.grid(row=4,column=4,padx=4)

b4=ttk.Button(root,text="Resize Image", width = 15,command=resize_func)
b4.grid(row=4,column=5,padx=4,pady=4)



break2=Label(root,text="____________________________________________________________________________________________",fg='#303F9F',bg="#e8f5e9",font='Calibri 11 bold')
break2.grid(row=5,column=0,padx=4,pady=1,columnspan=7)


#Image to PDF
l2=Label(root,text="IMAGE to PDF CONVERTER",fg='#303F9F',bg='#c8e6c9',font='Calibri 11 bold')
l2.grid(row=6,column=2,columnspan=3,pady=7)

b5=ttk.Button(root,text="Image to PDF", width = 15,command=pdf_convert)
b5.grid(row=7,column=2,columnspan=3)


break3=Label(root,bg="#e8f5e9",text="____________________________________________________________________________________________",fg='#303F9F',font='Calibri 11 bold')
break3.grid(row=8,column=0,padx=4,pady=1,columnspan=7)


l3=Label(root,text="DETECT FACE FROM IMAGE",fg='#303F9F',bg='#c8e6c9',font='Calibri 11 bold')
l3.grid(row=9,column=2,columnspan=3,pady=7)

b6=ttk.Button(root,text="DETECT FACE ", width = 15,command=face_detect)
b6.grid(row=10,column=2,columnspan=3)


break4=Label(root,bg="#e8f5e9",text="____________________________________________________________________________________________",fg='#303F9F',font='Calibri 11 bold')
break4.grid(row=11,column=0,padx=4,pady=1,columnspan=7)


l5=Label(root,text="ROTATE AN IMAGE",fg='#303F9F',bg='#c8e6c9',font='Calibri 11 bold')
l5.grid(row=12,column=2,columnspan=3,pady=7)

b7=ttk.Button(root,text="90 DEG ", width = 15,command=rotate_90)
b7.grid(row=13,column=2,padx=4,pady=4)

b8=ttk.Button(root,text="180 DEG ", width = 15,command=rotate_180)
b8.grid(row=13,column=3,padx=4,pady=4)

b9=ttk.Button(root,text="270 DEG ", width = 15,command=rotate_270)
b9.grid(row=13,column=4,padx=4,pady=4)


break5=Label(root,bg="#e8f5e9",text="____________________________________________________________________________________________",fg='#303F9F',font='Calibri 11 bold')
break5.grid(row=14,column=0,padx=4,pady=1,columnspan=7)

l5=Label(root,text="TAKE A PHOTO FROM WEBCAM",fg='#303F9F',bg='#c8e6c9',font='Calibri 11 bold')
l5.grid(row=15,column=2,columnspan=3,pady=4)

b10=ttk.Button(root,text="TAKE A PHOTO (Press Q)", width = 30,command=take_photo)
b10.grid(row=16,column=2,columnspan=3,padx=4,pady=0)


break6=Label(root,text="____________________________________________________________________________________________",fg='#303F9F',bg="#e8f5e9",font='Calibri 11 bold')
break6.grid(row=17,column=0,padx=4,pady=1,columnspan=7)

l6=Label(root,text="NOTE: IMAGES WILL BE SAVED IN C:\IMAGE_FORMATTING_APP",fg='#303F9F',bg='#c8e6c9',font='Calibri 11 bold')
l6.grid(row=18,column=0,columnspan=7,padx=0)

l7=Label(root,text="------Project Contributed By------",fg='#303F9F',bg='#c8e6c9',font='Calibri 11 bold')
l7.grid(row=19,column=0,columnspan=7,padx=1)

l8=Label(root,text="Rishi Jain( github.com/Rishi500 )",fg='#303F9F',bg='#c8e6c9',font='Calibri 11 bold')
l8.grid(row=20,column=0,columnspan=7,padx=2)
l9=Label(root,text="Krati Bhandari( github.com/Krati500 )",fg='#303F9F',bg='#c8e6c9',font='Calibri 11 bold')
l9.grid(row=21,column=0,columnspan=7,padx=2)
break6=Label(root,text="____________________________________________________________________________________________",fg='#303F9F',bg="#e8f5e9",font='Calibri 11 bold')
break6.grid(row=22,column=0,padx=4,pady=1,columnspan=7)

# Take a Photo From WebCam
# Image Rotate
# Detect Face from from images
root.mainloop()
