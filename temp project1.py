# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import*

root = Tk()
root.title("ADDITION")
root.geometry("500x500")

label2 = Label(text="ADDITION WINDOW")
label2.pack()


label = Label(text="<<RESULT>>")
label.pack()

b=20
 
def addition():
    global b
    b=b+10
    label["text"]= "THE ANSWER IS :   "+str(b)

def subtraction():
    global b
    b=b-10
    label["text"]= "THE ANSWER IS :   "+str(b)

def multiplication():
    global b
    b=b*10
    label["text"]= "THE ANSWER IS :   "+str(b)

def division():
    global b
    b=b/10
    label["text"]= "THE ANSWER IS :   "+str(b)
    
button = Button(root,text="ADD DATA",command=addition)
button.pack()

print()

button = Button(root,text="SUB DATA",command=subtraction)
button.pack()


button = Button(root,text="MUL DATA",command=multiplication)
button.pack()


button = Button(root,text="DIV DATA",command=division)
button.pack()



root.mainloop()