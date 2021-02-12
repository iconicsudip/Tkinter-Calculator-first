from tkinter import *

root=Tk()
root.title("CALCULATOR")
root.iconbitmap('calculator.ico')

#label
b=Entry(root,width=40,borderwidth=6)
b.grid(row=0,column=0,columnspan=3,padx=10,pady=5)

def click(number):
    c=b.get()
    b.delete(0,END)
    b.insert(0,str(c)+str(number))

def add():
    f_number=b.get()
    global f_num
    global math
    math="addition"
    f_num=int(f_number)
    b.delete(0,END)

def sub():
    f_number = b.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(f_number)
    b.delete(0, END)

def div():
    f_number = b.get()
    global f_num
    global math
    math = "division"
    f_num = int(f_number)
    b.delete(0, END)

def mul():
    f_number = b.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(f_number)
    b.delete(0, END)

def clear():
    b.delete(0,END)

def equal():
    s_number=b.get()
    b.delete(0,END)
    if math=="addition":
        b.insert(0,f_num + int(s_number))
    if math=="subtraction":
        b.insert(0,f_num - int(s_number))
    if math=="division":
        b.insert(0,f_num / int(s_number))
    if math=="multiply":
        b.insert(0,f_num * int(s_number))

button_1=Button(root,text="1",padx=40,pady=10,command=lambda: click(1))
button_2=Button(root,text="2",padx=40,pady=10,command=lambda: click(2))
button_3=Button(root,text="3",padx=40,pady=10,command=lambda: click(3))
button_4=Button(root,text="4",padx=40,pady=10,command=lambda: click(4))
button_5=Button(root,text="5",padx=40,pady=10,command=lambda: click(5))
button_6=Button(root,text="6",padx=40,pady=10,command=lambda: click(6))
button_7=Button(root,text="7",padx=40,pady=10,command=lambda: click(7))
button_8=Button(root,text="8",padx=40,pady=10,command=lambda: click(8))
button_9=Button(root,text="9",padx=40,pady=10,command=lambda:click(9))
button_0=Button(root,text="0",padx=40,pady=10,command=lambda:click(0))
button_a=Button(root,text="+",padx=39,pady=10,command=lambda:add())
button_b=Button(root,text="-",padx=40,pady=10,command=lambda:sub())
button_c=Button(root,text="*",padx=40,pady=10,command=lambda:mul())
button_d=Button(root,text="/",padx=40,pady=10,command=lambda:div())
button_e=Button(root,text="=",padx=39,pady=10,command=lambda:equal())
button_f=Button(root,text="CLEAR",width=40,command=lambda:clear())

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_a.grid(row=4,column=1)
button_b.grid(row=4,column=2)
button_c.grid(row=5,column=0)
button_d.grid(row=5,column=1)
button_e.grid(row=5,column=2)

button_f.grid(row=6,column=0,columnspan=3,padx=2,pady=2)

button=Button(root,text="CLOSE",width=40,command=root.quit)
button.grid(row=7,column=0,columnspan=3)



root.mainloop()