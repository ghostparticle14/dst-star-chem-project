from  tkinter import *
from subprocess import call
import tkinter.messagebox
import tkinter.scrolledtext
#import tkcolorpicker
import os


#import PyPDF2



import time
import sys
import datetime

root=Tk()


#t = textract.process(root.file)
#print(t)


#toolbar = Label(root, text="Tool Bar", bd=1, relief=SUNKEN, anchor=W)
#toolbar.pack(side=TOP, fill=X)

frame=Frame(root)
frame.pack()

#color=tkcolorpicker.askcolor(color="red", parent=None, title=("Color Chooser"), alpha=False)
#print(color)


mylist=[]
today=datetime.date.today()
mylist.append(today)

time_string=''

def tick():
    # get the current local time from the PC
    time_string = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    statusbar.config(text="Status Bar        "+str(mylist[0])+'\t'+time_string)
    statusbar.after(200, tick)

#root = Tk()
#clock = (frame, font=('times', 20, 'bold'))
#clock.grid(row=7, sticky=S) 
statusbar = Label(root, text="Status Bar        "+str(mylist[0]), bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)
tick()
#root.mainloop()

def open1(event):

    root.file =  filedialog.askopenfilename(initialdir = "/home/hp/python",title = \
    "choose your file",filetypes = (("Python files","*.py"),("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    #file = open(root.file)
    #data = file.read()
    #file.close()
    #Results = Label(frame, text = data)
    #Results.grid(row = 8)
    call(['xdg-open',root.file])
    print(root.file)
    
def searchS(event):
    
    root.file =  filedialog.askopenfilename(initialdir = "/home/hp",title = \
    "choose your file",filetypes = (("Text files","*.txt"),("Python files","*.py"),("PDF files","*.pdf"),("LibreOffice Writer files","*.odt"),("all files","*.*")))
        #p = Popen(cmd, stdout=PIPE)
        #stdout, stderr = p.communicate()
    def replace1(string):
        return string.replace('.pdf', '.txt')

    
    if (root.file[-4:] == '.pdf'):
        os.system(('pdftotext %s') % root.file)
        filepath=replace1(root.file)
        

    '''with open(filepath, encoding='utf-8') as f:
        data=f.read()
        filepath.replace('.pdf','.txt')'''

    #root.file.replace(".pdf",".txt")
    
    print(filepath)
    file = open(filepath)
    data = file.read()
    file.close()
    
    def find():
        count=0
        text.tag_remove('found', '1.0', END)
        s = edit.get()
        if s:
            idx = '1.0'
            while 1:
                idx = text.search(s, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                text.tag_add('found', idx, lastidx)
                idx = lastidx
                count+=1
            text.tag_config('found', foreground='red')
        tkinter.messagebox.showinfo('Search', "Your Search Query Was Found "+str(count)+" Times",parent=root2)
        edit.focus_set()

    
    root2=Toplevel()   

    fram = Frame(root2)
    
    Label(fram,text='Text to find:').pack(side=LEFT)
    edit = Entry(fram)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    butt = Button(fram, text='Find')
    butt.pack(side=RIGHT)
    fram.pack(side=TOP)
    
    text = Text(root2, font='consolas 12')
    text.insert('1.0',data)
    text.pack(side=BOTTOM)
    butt.config(command=find)


    #scrollb = Scrollbar(root2, command=text.yview)
    #scrollb.pack(side=RIGHT)
    #text['yscrollcommand'] = scrollb.set

    root2.mainloop()


def exit1(event):
    
    ques = tkinter.messagebox.askquestion('Prompt : ', "Do you really want to exit?")
    if ques == 'yes':
        root.withdraw()
    else:
        root.mainloop()

'''


def open2():

    root.file =  filedialog.askopenfilename(initialdir = "/home/hp/python",title = \
    "choose your file",filetypes = (("Python files","*.py"),("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    #file = open(root.file)
    #data = file.read()
    #file.close()
    #Results = Label(frame, text = data)
    #Results.grid(row = 8)
    call(['xdg-open',root.file])
    print(root.file)

def search2():
    
    root.file =  filedialog.askopenfilename(initialdir = "/home/hp/python",title = \
    "choose your file",filetypes = (("Python files","*.py"),("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))
    file = open(root.file)
    data = file.read()
    file.close()
    #Results = Label(frame, text = data)
    #Results.grid(row = 8)
    #call(['xdg-open',root.file])
    #print(root.file)
    #import sys
    #sys.path.append('/home/hp/Desktop/GUI/windowSearch.py/')
    def find():
        text.tag_remove('found', '1.0', END)
        s = edit.get()
        if s:
            idx = '1.0'
            while 1:
                idx = text.search(s, idx, nocase=1, stopindex=END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                text.tag_add('found', idx, lastidx)
                idx = lastidx
            text.tag_config('found', foreground='red')
        edit.focus_set()

    
    root2=Toplevel()   

    fram = Frame(root2)
    Label(fram,text='Text to find:').pack(side=LEFT)
    edit = Entry(fram)
    edit.pack(side=LEFT, fill=BOTH, expand=1)
    edit.focus_set()
    butt = Button(fram, text='Find')
    butt.pack(side=RIGHT)
    fram.pack(side=TOP)
    
    text = Text(root2)
    text.insert('1.0',data)
    text.pack(side=BOTTOM)
    butt.config(command=find)
    root2.mainloop()

def exit2():
    
    ques = tkinter.messagebox.askquestion('Prompt : ', "Do you really want to exit?")
    if ques == 'yes':
        root.withdraw()
    else:
        root.mainloop()
'''















def Time(event):
    currenttime = datetime.datetime.now()
    tkinter.messagebox.showinfo('Time', currenttime)


photo = PhotoImage(file="Python_icon.png")
label = Label(frame, image=photo)
label.grid(row=0, column=0)

#statusbar = App.__init__()

l2=Label(frame, text="\nDBT Star College Scheme\n\nPython Project : Search Box\n", font=("Comic Sans MS", 30))
l2.grid(row=1, column=0, stick='N')

search=Button(frame, text="Search a STRING", font='ariel 15', fg='white', bg="blue")
search.bind("<Button-1>", searchS)
search.grid(row=3, column=0)

search1=Button(frame, text="Open a file", font='ariel 15', fg='white', bg="blue")
search1.bind("<Button-1>", open1)
search1.grid(row=4, column=0)

l=Label(frame, text='', font='ariel 15')
l.grid(row=5)

stop=Button(frame, text="    Exit    ", font='ariel 15', fg='white', bg="blue")
stop.bind("<Button-1>", exit1)
stop.grid(row=6)

#l2=Label(frame, text='\n\n\n\n\n\n', font='ariel 15')
#l2.grid(row=6)

#time=Button(frame, text="Time", font='ariel 12')
#time.bind("<Button-1>", Time)
#time.grid(row=7)

'''menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="Options", menu=submenu)
submenu.add_command(label="Open a file", command=open2)
submenu.add_command(label="Search a STRING", command=search2)
submenu.add_separator()
submenu.add_command(label="Exit", command=exit2)'''


root.mainloop()
