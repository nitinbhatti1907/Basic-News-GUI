# Title :- Basic News GUI
# Discription :- The Tkinter library in Python provides a way to create GUI (Graphical User Interface) applications. One use case for a GUI application is to display news headlines and Images, which can be easily achieved by creating a basic news GUI using Tkinter. This application typically includes a main window, labels to display news headlines, image widge to display the image of the news and also a button that use to move the next news. The GUI can be designed using various Tkinter widgets, such as labels, text widgets, and buttons to create a user-friendly interface for accessing and reading news articles.This is a project version that only specify those news items whose are present in txt file and news_pic folder.

from tkinter import *
from PIL import ImageTk,Image
import os

# Create a GUI window
root = Tk()
root.title("Basic News Viewer")

def loop_news():
    '''
    funcion use for print headlines based on the news images and move next
    '''

    global count
    global counter
    img_label.config(image=img_array[count%len(img_array)]) #--> For images change
    count+=1
    info.config(text=news_array[counter%len(news_array)]) #--> For headlines change
    counter+=1

count = 0
root.geometry("350x550")
root.resizable(0,0)

# Assign the title on top of images.
name = Label(root,text="Top News",bg='black',fg='white',font='verdana 15 bold')
name.pack(pady=20)

# Read the images from folder one by one.
files = os.listdir('news pic')
img_array=[]
for file in files:
    img = Image.open(os.path.join('news pic',file))
    resized_img = img.resize((250,200))
    img_array.append(ImageTk.PhotoImage(resized_img))

# Assign images on the GUI window.
img_label = Label(root,image=img_array[0])
img_label.pack(pady=20)

# Read the Headlines from news details.txt file based on images.
file1 = open('news details.txt', 'r')
Lines = file1.readlines()
counter=0
news_array=[]
for line in Lines:
    counter+=1
    news = "News{}: {}".format(counter, line.strip())
    news_array.append(news)

# Assign headlines on the GUI window.
info = Label(root,text=news_array[0],fg='black',justify='center',font='verdana 15',wraplength=350)
info.pack(pady=10)

# Assign Next buttton for move to the next news.
next_btn = Button(root,text="Next",bg="white",fg="black",font="verdana 15",command=loop_news)
next_btn.pack()

root.mainloop()