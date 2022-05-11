# Main Objective : to solve atleast basic arithmetic problems via voice recognition 
# 				 : making buttons show up / disappear when Scie Button is pressed 
# 				 : using eval() to solve any equations 
import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from voiceInput import *
from textAnalyzer import *
import math
import re



val=""   
operators = ["+", "-", "*", "/", "%", "("]

def voice_actions(arr):
	global val
	A = 0
	operator = arr[0]
	op1 = arr[1]
	op2 = arr[2]

	if operator == "+":
		A = int(op1) + int(op2)
	
	if operator == "-":
		A = int(op1) - int(op2)

	if operator in  ["*", "into", "x", "multiply by", "multiply", "times", "x", "time"]:
		A = int(op1) * int(op2)

	if operator == "/" or operator == "divided by" or operator == "divided" or operator == "divide":
		A = int(op1) / int(op2)
	if operator == "factorial":
		A = math.factorial(op2)
	
	val = str(A)
	data.set(val)


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
	global val
	
	val=val + "+"
	data.set(val)

def pressed_Minus():
	global val
	
	val=val + "-"
	data.set(val)

def pressed_Div():
	global val
	
	val=val + "/"
	data.set(val)

def pressed_C():
	global val
	val=""
	data.set(val)

def pressed_Mul():
	global val
	
	val=val + "*"
	data.set(val)


def pressed_btnV():
	global val
	data.set("Speak Now...")
	text = v_input()
	print(text)
	val = text
	data.set(val)
	arr = analyze(text) #array of operands and operator
	print(arr)
	voice_actions(arr)
	

def pressed_dot():
	global val
	val = val + "."
	data.set(val)

def pressed_percent():
	global val

	val = val + "%"
	data.set(val)

def pressed_btnB():
	global val
	l = len(val)
	if val[l-5:] in [" cos(", " sin(", " log(", " tan("]:
		val = val[:l-5]
	else:
		val = val[:-1]
	data.set(val)

def pressed_LB():
	global val
	
	val += "("
	data.set(val)

def pressed_RB():
	global val
	
	val += ")"
	data.set(val)

def result():
	global val

	while "π" in val:
		val = val.replace("π", "math.pi")
	while " sin" in val:
		val = val.replace(" sin", "math.sin")	
	while " cos" in val:
		val = val.replace(" cos", "math.cos")		
	while " tan" in val:
		val = val.replace(" tan", "math.tan")
	while " log" in val:
		val = val.replace(" log", "math.log")
	while "%" in val:
		val = val.replace("%", "* 0.01")
	while "!" in val:
		pat = re.compile(r"\d+(?<=)!")
		n = re.search(pat, val)
		str1 = val[n.start():n.end()]
		num = val[n.start():n.end()-1]
		rep = "math.factorial(" + num + ")"
		val = val.replace(str1, rep)

	
	val = str(eval(val))
	data.set(val)


def S_fact():
	global val

	val += "!"
	data.set(val)

def S_sin():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"

	val += " sin("
	
	data.set(val)



def S_cos():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	val += " cos("
	data.set(val)

def S_tan():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	val += " tan("

	data.set(val)

def S_log():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	
	val += " log("
	data.set(val)

def S_pi():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	val += "π"
	data.set(val)

	
root= tk.Tk()
root.geometry("400x600+800+25")
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
		btnPi=Button(btnrowS1,text="π",font=("Arial",12),border=0.5,relief=GROOVE, command = S_pi)
		btnPi.pack(side = LEFT,expand=True,)
		btnFact=Button(btnrowS1,text="n!",font=("Verdana",12),border=0.5,relief=GROOVE, command = S_fact)
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

btnLB=Button(btnrow00,text="(",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_LB)
btnLB.pack(side = LEFT,expand=True,fill="both",)
btnRB=Button(btnrow00,text=")",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_RB)
btnRB.pack(side = LEFT,expand=True,fill="both",)
btnMod=Button(btnrow00,text="%",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_percent)
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
btn_AC=Button(btnrow4,text="AC",font=("Verdana",22),border=0,relief=GROOVE,command= pressed_C)
btn_AC.pack(side = LEFT,expand=True,fill="both",)
btnEq=Button(btnrow4,text="=",font=("Verdana",22),border=0,fg = "sea green" ,relief=GROOVE,command= result)
btnEq.pack(side = LEFT,expand=True,fill="both",)

root.mainloop()