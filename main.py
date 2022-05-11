# Main Objective : Adding Backspace, Buttons for Voice, Scientific Calc, Percentage, decimal, brackets etc

import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from voiceInput import *
from textAnalyzer import *
import math
import re



val=""   
A = 0
operator = ""

def voice_actions(arr):
	global A
	operator = arr[0]
	op1 = arr[1]
	op2 = arr[2]
	if operator == "+":
		A = int(op1) + int(op2)
	
	if operator == "-":
		A = int(op1) - int(op2)

	if operator == "*" or operator == "into" or operator == "x" or operator == "multiply by" or operator == "multiply":
		A = int(op1) * int(op2)

	if operator == "/" or operator == "divided by" or operator == "divided" or operator == "divide":
		A = int(op1) / int(op2)
	
	A = str(A)
	data.set(A)

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
	try:
		A=int(val)
	except:
		A=float(val)
	operator="+"
	val=val + "+"
	data.set(val)

def pressed_Minus():
	global A
	global operator
	global val
	try:
		A = int(val)
	except:
		A = float(val)
	operator="-"
	val=val + "-"
	data.set(val)

def pressed_Div():
	global A
	global operator
	global val
	try:
		A = int(val)
	except:
		A = float(val)	
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
	try:
		A=int(val)
	except:
		A=float(val)
	operator="*"
	val=val + "*"
	data.set(val)


def pressed_btnV():
	data.set("Speak Now...")
	text = v_input()
	print(text)
	data.set(text)
	arr = analyze(text) #array of operands and operator
	print(arr)
	voice_actions(arr)

def pressed_dot():
	global A
	global operator
	global val
	val = val + "."
	data.set(val)

def pressed_btnB():
	global A
	global operator
	global val
	val = val[:-1]
	data.set(val)
 	
def pressed_bracket():

	global A
	global operator
	global val
	last = 0
	for i in val:
		if i == "(":
			last = "("
		if i == ")":
			last = ")"
	if last == 0 or last == ")":
		val += "("
	else:
		val += ")"
	data.set(val)
def result():
	global A
	global operator
	global val
	val2 = val
	
	if operator == "+" :
		try:
			x = int((val2.split("+")[1]))
		except:
			x = float((val2.split("+")[1]))
		C=A+x
		data.set(C)
		val = str(C)

	elif operator == "-" :
		try:
			x = int((val2.split("-")[1]))
		except:
			x = float((val2.split("-")[1]))	
		C=A-x
		data.set(C)
		val = str(C)

	elif operator == "*" :
		try:
			x = int((val2.split("*")[1]))
		except:
			x = float((val2.split("*")[1]))
		C=A*x
		data.set(C)
		val = str(C)

	if operator == "/" :
		try:
			x = int((val2.split("/")[1]))
		except:
			x = float((val2.split("/")[1]))
		
		if x == 0 :
			messagebox.showerror("Error","Division with 0 is NOT supported")
			A=0
			val=""
			data.set(val)
		else:	 
			C=A/x
			data.set(C)
			val = str(C)
	if operator == "sin":
		pat = re.compile(r"(?<=sin\()\d+")
		n = re.search(pat, val)
		num = float(val[n.start():n.end()])
		val = str(math.sin(num))
		data.set(val)
	if operator == "cos":
		pat = re.compile(r"(?<=cos\()\d+")
		n = re.search(pat, val)
		num = float(val[n.start():n.end()])
		val = str(math.cos(num))
		data.set(val)
	if operator == "tan":
		pat = re.compile(r"(?<=tan\()\d+")
		n = re.search(pat, val)
		num = float(val[n.start():n.end()])
		val = str(math.tan(num))
		data.set(val)
	if operator == "log":
		pat = re.compile(r"(?<=log\()\d+")
		n = re.search(pat, val)
		num = float(val[n.start():n.end()])
		val = str(math.log(num))
		data.set(val)
def S_sin():
	global A
	global operator
	global val

	operator = "sin"
	val += "sin("
	
	data.set(val)
def S_cos():
	global A
	global operator
	global val


	operator = "cos"
	val += "cos("
	data.set(val)

def S_tan():
	global A
	global operator
	global val

	operator = "tan"
	val += "tan("

	data.set(val)

def S_log():
	global A
	global operator
	global val

	
	operator = "log"
	val += "log("
	data.set(val)

	
root= tk.Tk()
root.geometry("400x600+25+25")
root.resizable(0,0)
root.title("Calculator")
data = StringVar()
lbl=Label(root,height = "4",justify = "right",textvariable=data,font=("Verdana",18),anchor=SE,bg="#b7b7b7")
lbl.pack(expand=True,fill="both",)

scientific = 0

def scie():
	global scientific
	global btnrowS1
	if scientific == 0:
		scientific = 1
		btnrowS1 = Frame(root, bg="#b7b7b7" )
		btnrowS1.pack(expand=True, fill ="both",)

		btnSin=Button(btnrowS1,text="sin",font=("Verdana",12),border=0.5,relief=GROOVE, command = S_sin)
		btnSin.pack(side = LEFT,expand=True,)
		btnCos=Button(btnrowS1,text="cos",font=("Verdana",12),border=0.5,relief=GROOVE, command = S_cos)
		btnCos.pack(side = LEFT,expand=True,)
		btnTan=Button(btnrowS1,text="tan",font=("Verdana",12),border=0.5,relief=GROOVE, command = S_tan)
		btnTan.pack(side = LEFT,expand=True,)
		btnPi=Button(btnrowS1,text="π",font=("Arial",12),border=0.5,relief=GROOVE)
		btnPi.pack(side = LEFT,expand=True,)
		btnFact=Button(btnrowS1,text="n!",font=("Verdana",12),border=0.5,relief=GROOVE)
		btnFact.pack(side = LEFT,expand=True,)
		btnLog=Button(btnrowS1,text="log",font=("Verdana",12),border=0.5,relief=GROOVE, command = S_log)
		btnLog.pack(side = LEFT,expand=True,)
	else:
		scientific = 0
		btnrowS1.destroy()
		btnrowS1 = Frame(root)

btnrow0 = Frame(root)
btnrow0.pack(expand=True, fill ="both",)
btnS=Button(btnrow0,text="Scie",font=("Verdana",12),border=1,fg = "white" ,bg = "#000055",relief=GROOVE,command = scie)
btnS.pack(side = LEFT,expand=True,)

btnV=Button(btnrow0,text="Voice",font=("Verdana",12),border=1,fg = "white" ,bg = "#000055",relief=GROOVE, command = pressed_btnV)
btnV.pack(side = LEFT,expand=True,)

btnB=Button(btnrow0,text="<--",font=("Verdana",12),border=1,fg = "white" ,bg = "dark red",relief=GROOVE,command = pressed_btnB)
btnB.pack(side = LEFT,expand=True,)

btnrow00 = Frame(root,bg="#000000")
btnrow00.pack(expand=True , fill ="both",)

btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand=True , fill ="both",)
btnrow2 = Frame(root,)
btnrow2.pack(expand=True , fill ="both",)
btnrow3 = Frame(root,)
btnrow3.pack(expand=True , fill ="both",)
btnrow4 = Frame(root,)
btnrow4.pack(expand=True , fill ="both",)

btnrowS1 = Frame()

btnAC=Button(btnrow00,text="AC",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_C)
btnAC.pack(side = LEFT,expand=True,fill="both",)
btnB=Button(btnrow00,text="<--",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btnB)
btnB.pack(side = LEFT,expand=True,fill="both",)
btnMod=Button(btnrow00,text="%",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn1)
btnMod.pack(side = LEFT,expand=True,fill="both",)
btnDiv=Button(btnrow00,text="/",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_Div)
btnDiv.pack(side = LEFT,expand=True,fill="both",)




btn7=Button(btnrow1,text="7",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn7)
btn7.pack(side = LEFT,expand=True,fill="both",)
btn8=Button(btnrow1,text="8",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn8)
btn8.pack(side = LEFT,expand=True,fill="both",)
btn9=Button(btnrow1,text="9",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn9)
btn9.pack(side = LEFT,expand=True,fill="both",)
btnMul=Button(btnrow1,text="*",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_Mul)
btnMul.pack(side = LEFT,expand=True,fill="both",)



btn4=Button(btnrow2,text="4",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn4)
btn4.pack(side = LEFT,expand=True,fill="both",)
btn5=Button(btnrow2,text="5",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn5)
btn5.pack(side = LEFT,expand=True,fill="both",)
btn6=Button(btnrow2,text="6",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn6)
btn6.pack(side = LEFT,expand=True,fill="both",)
btnMinus=Button(btnrow2,text="-",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_Minus)
btnMinus.pack(side = LEFT,expand=True,fill="both",)

btn1=Button(btnrow3,text="1",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn1)
btn1.pack(side = LEFT,expand=True,fill="both",)
btn2=Button(btnrow3,text="2",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn2)
btn2.pack(side = LEFT,expand=True,fill="both",)
btn3=Button(btnrow3,text="3",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn3)
btn3.pack(side = LEFT,expand=True,fill="both",)
btnPlus=Button(btnrow3,text="+",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_Plus)
btnPlus.pack(side = LEFT,expand=True,fill="both",)


btn_dot=Button(btnrow4,text=".",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_dot)
btn_dot.pack(side = LEFT,expand=True,fill="both",)
btn0=Button(btnrow4,text="0",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_btn0)
btn0.pack(side = LEFT,expand=True,fill="both",)
btn_bracket=Button(btnrow4,text="()",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_bracket)
btn_bracket.pack(side = LEFT,expand=True,fill="both",)
btnEq=Button(btnrow4,text="=",font=("Verdana",22),border=0,fg = "sea green" ,relief=GROOVE,command= result)
btnEq.pack(side = LEFT,expand=True,fill="both",)

root.mainloop()