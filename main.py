# Main Task : Designing a basic layout of the Application ("Laying the Foundation")
import tkinter as tk 
from tkinter import *
from tkinter import messagebox

val=""
A = 0
operator = ""

def pressed_btn1():
	global val
	val=val+"1"
	data.set(val)

def pressed_btn2():
    global val
    val=val+"2"
    data.set(val) 	

def pressed_btn3():
	global val
	val=val+"3"
	data.set(val)

def pressed_btn4():
	global val
	val=val+"4"
	data.set(val)

def pressed_btn5():
	global val
	val=val+"5"
	data.set(val)	

def pressed_btn6():
	global val
	val=val+"6"
	data.set(val)

def pressed_btn7():
	global val
	val=val+"7"
	data.set(val)

def pressed_btn8():
	global val
	val=val+"8"
	data.set(val)

def pressed_btn9():
	global val
	val=val+"9"
	data.set(val)

def pressed_btn0():
	global val
	val=val+"0"
	data.set(val)

def pressed_Plus():
	global A
	global operator
	global val
	A=int(val)
	operator="+"
	val=val + "+"
	data.set(val)

def pressed_Minus():
	global A
	global operator
	global val
	A=int(val)
	operator="-"
	val=val + "-"
	data.set(val)

def pressed_Div():
	global A
	global operator
	global val
	A=int(val)
	operator="/"
	val=val + "/"
	data.set(val)


def pressed_C():
	global A
	global val
	global operator

	A=0
	val=""
	operator=""
	data.set(val)

def pressed_Mul():
	global A
	global operator
	global val
	A=int(val)
	operator="*"
	val=val + "*"
	data.set(val)
	
def result():
	global A
	global operator
	global val
	val2 = val
	
	if operator == "+" :
		x = int((val2.split("+")[1]))
		C=A+x
		data.set(C)
		val = str(C)

	elif operator == "-" :
		x = int((val2.split("-")[1]))
		C=A-x
		data.set(C)
		val = str(C)

	elif operator == "*" :
		x = int((val2.split("*")[1]))
		C=A*x
		data.set(C)
		val = str(C)

	if operator == "/" :
		x = int((val2.split("/")[1]))
		
		if x == 0 :
			messagebox.showerror("Error","Division with 0 is NOT supported")
			A=0
			val=""
			data.set(val)
		else:	 
			C=int(A/x)
			data.set(C)
			val = str(C)
	
root= tk.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")
data = StringVar()
lbl=Label(root,textvariable=data,font=("Verdana",20),anchor=SE,bg="#b7b7b7")
lbl.pack(expand=True,fill="both",)

btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand=True , fill ="both",)
btnrow2 = Frame(root,)
btnrow2.pack(expand=True , fill ="both",)
btnrow3 = Frame(root,)
btnrow3.pack(expand=True , fill ="both",)
btnrow4 = Frame(root,)
btnrow4.pack(expand=True , fill ="both",)


btn1=Button(btnrow1,text="1",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn1)
btn1.pack(side = LEFT,expand=True,fill="both",)
btn2=Button(btnrow1,text="2",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn2)
btn2.pack(side = LEFT,expand=True,fill="both",)
btn3=Button(btnrow1,text="3",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn3)
btn3.pack(side = LEFT,expand=True,fill="both",)
btnPlus=Button(btnrow1,text="+",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_Plus)
btnPlus.pack(side = LEFT,expand=True,fill="both",)


btn4=Button(btnrow2,text="4",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn4)
btn4.pack(side = LEFT,expand=True,fill="both",)
btn5=Button(btnrow2,text="5",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn5)
btn5.pack(side = LEFT,expand=True,fill="both",)
btn6=Button(btnrow2,text="6",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn6)
btn6.pack(side = LEFT,expand=True,fill="both",)
btnMinus=Button(btnrow2,text="-",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_Minus)
btnMinus.pack(side = LEFT,expand=True,fill="both",)

btn7=Button(btnrow3,text="7",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn7)
btn7.pack(side = LEFT,expand=True,fill="both",)
btn8=Button(btnrow3,text="8",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn8)
btn8.pack(side = LEFT,expand=True,fill="both",)
btn9=Button(btnrow3,text="9",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn9)
btn9.pack(side = LEFT,expand=True,fill="both",)
btnMul=Button(btnrow3,text="*",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_Mul)
btnMul.pack(side = LEFT,expand=True,fill="both",)

btnC=Button(btnrow4,text="C", fg = "Red",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_C)
btnC.pack(side = LEFT,expand=True,fill="both",)
btn0=Button(btnrow4,text="0",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn0)
btn0.pack(side = LEFT,expand=True,fill="both",)
btnEq=Button(btnrow4,text="=",font=("Verdana",22),border=0,relief=GROOVE,command= result)
btnEq.pack(side = LEFT,expand=True,fill="both",)
btnDiv=Button(btnrow4,text="/",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_Div)
btnDiv.pack(side = LEFT,expand=True,fill="both",)
root.mainloop()