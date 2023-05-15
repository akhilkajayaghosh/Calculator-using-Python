import tkinter as tk
window=tk.Tk()
window.geometry("500x600")
window.configure(bg="#313E2C")
window.resizable(False,False)
window.title("Calculator")
expression=""
def show(val):
    global expression
    expression+=str(val)
    Label.configure(text=expression)
def clear():
    global expression
    expression=""
    Label.configure(text=expression)
def bk():
    global expression
    expression=expression[0:-1]
    Label.configure(text=expression)
def calculate():
    global expression
    result=""
    if expression!="":
        try:
            result=eval(expression)    
        except:
            result="Error" 
            expression=""
    Label.configure(text=result)
    expression=str(result)
    

Label= tk.Label(window,text="",font=('calibre',25,'normal'),width=23,height=2)
Label.place(x=20,y=20)
b16=tk.Button(window, text="CLEAR",width=30,height=4,bg="#B42507",activebackground="#B42507",command=lambda:clear()).place(x=20,y=120)
b16=tk.Button(window, text="⌫",width=30,height=4,command=lambda:bk()).place(x=240,y=120)

b1=tk.Button(window, text="7",width=14,height=4,command=lambda:show('7')).place(x=20,y=200)
b2=tk.Button(window, text="8",width=14,height=4,command=lambda:show('8')).place(x=130,y=200)
b3=tk.Button(window, text="9",width=14,height=4,command=lambda:show('9')).place(x=240,y=200)
b4=tk.Button(window, text="/",width=14,height=4,command=lambda:show('/')).place(x=350,y=200)

b5=tk.Button(window, text="4",width=14,height=4,command=lambda:show('4')).place(x=20,y=280)
b6=tk.Button(window, text="5",width=14,height=4,command=lambda:show('5')).place(x=130,y=280)
b7=tk.Button(window, text="6",width=14,height=4,command=lambda:show('6')).place(x=240,y=280)
b8=tk.Button(window, text="X",width=14,height=4,command=lambda:show('*')).place(x=350,y=280)

b9=tk.Button(window, text="1",width=14,height=4,command=lambda:show('1')).place(x=20,y=360)
b10=tk.Button(window, text="2",width=14,height=4,command=lambda:show('2')).place(x=130,y=360)
b11=tk.Button(window, text="3",width=14,height=4,command=lambda:show('3')).place(x=240,y=360)
b12=tk.Button(window, text="-",width=14,height=4,command=lambda:show('-')).place(x=350,y=360)

b13=tk.Button(window, text=".",width=14,height=4,command=lambda:show('.')).place(x=20,y=440)
b14=tk.Button(window, text="0",width=14,height=4,command=lambda:show('0')).place(x=130,y=440)
b15=tk.Button(window, text="=",width=14,height=4,bg="#2E6E16",activebackground="#2E6E16",command=lambda:calculate()).place(x=240,y=440)
b16=tk.Button(window, text="+",width=14,height=4,command=lambda:show('+')).place(x=350,y=440)

window.mainloop()