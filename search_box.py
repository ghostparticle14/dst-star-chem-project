from  tkinter import *
from subprocess import call
import tkinter.messagebox
#import tkColorChooser



#import time
import datetime

root=Tk()

#toolbar = Label(root, text="Tool Bar", bd=1, relief=SUNKEN, anchor=W)
#toolbar.pack(side=TOP, fill=X)

frame=Frame(root)
frame.pack()

#result = tkColorChooser.askcolor(color, option=value)

mylist=[]
today=datetime.date.today()
mylist.append(today)

def open1(event):
    
    root.file =  filedialog.askopenfilename(initialdir = "/home/hp/python",title = \
    "choose your file",filetypes = (("Python files","*.py"),("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    #file = open(root.file)
    #data = file.read()
    #file.close()
    #Results = Label(frame, text = data)
    #Results.grid(row = 8)
    call(['xdg-open',root.file])
    #print(root.file)

def exit1(event):
    
    ques = tkinter.messagebox.askquestion('Prompt : ', "Do you really want to exit?")
    if ques == 'yes':
        root.withdraw()
    else:
        root.mainloop()

def Time(event):
    currenttime = datetime.datetime.now()
    tkinter.messagebox.showinfo('Time', currenttime)


photo = PhotoImage(file="Python_icon.png")
label = Label(frame, image=photo)
label.grid(row=0, column=0)

statusbar = Label(root, text="Status Bar        "+str(mylist[0]), bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)
#statusbar = App.__init__()

l2=Label(frame, text="\nDBT Star College Scheme\n\nPython Project : Search Box\n", font='ariel 30')
l2.grid(row=1, column=0, stick='N')

search=Button(frame, text="Open a file", font='ariel 15', fg='white', bg='blue')
search.bind("<Button-1>", open1)
search.grid(row=3, column=0)

l=Label(frame, text='', font='ariel 15')
l.grid(row=4)

stop=Button(frame, text="    Exit    ", font='ariel 15', fg='white', bg='blue')
stop.bind("<Button-1>", exit1)
stop.grid(row=5)

l2=Label(frame, text='\n\n\n\n\n\n', font='ariel 15')
l2.grid(row=6)

time=Button(frame, text="Time", font='ariel 12')
time.bind("<Button-1>", Time)
time.grid(row=7)


#root.mainloop()
