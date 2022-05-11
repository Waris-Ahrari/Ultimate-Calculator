# Main Objective: Word Wrap, API, Added Dark Mode

import tkinter as tk
import scipy as sp
import scipy as sp
import numpy as np
import wolframalpha
from tkinter import *
from tkinter import messagebox
from voiceInput import *
from textAnalyzer import *
import math
import re
wolfram_id = "P6QTR6-V472P88E8G"



val=""   
mode = 0
operators = ["+", "-", "*", "/", "%", "("]


def smart_size(txt):
	global lbl
	req = lbl.winfo_reqwidth()

	l = len(txt)
	if l > 50:
		txt = txt[:l-50] + "\n" + txt[l-50:]
	if l > 25:
		txt = txt[:l-25] + "\n" + txt[l-25:]

	data.set(txt)


def search(text):
	client = wolframalpha.Client(wolfram_id)
	res = client.query(text)
	try:
		output = next(res.results)
		print(output.scanner)
		if output.scanner in ["Simplification","Statistics","NaturalMath" ,"Integral", "Numeric", "Derivative", "Reduce", "Identity", "Rational"]:
			print(output.text)
			smart_size(output.text)
		else:
			print(output.text)
			smart_size("I can not Answer that..")
	except:
		smart_size("Retry !")
	

def pressed_btnV():
	global val
	smart_size("Speak Now...")
	text = v_input()
	print(text)
	search(text)


	
	
	


def pressed_btn1():
	global val
	val=val+"1"
	smart_size(val)

def pressed_btn2():
    global val
    val=val+"2"
    smart_size(val) 	

def pressed_btn3():
	global val
	val=val+"3"
	smart_size(val)

def pressed_btn4():
	global val
	val=val+"4"
	smart_size(val)

def pressed_btn5():
	global val
	val=val+"5"
	smart_size(val)	

def pressed_btn6():
	global val
	val=val+"6"
	smart_size(val)

def pressed_btn7():
	global val
	val=val+"7"
	smart_size(val)

def pressed_btn8():
	global val
	val=val+"8"
	smart_size(val)

def pressed_btn9():
	global val
	val=val+"9"
	smart_size(val)

def pressed_btn0():
	global val
	val=val+"0"
	smart_size(val)



def pressed_Plus():
	global val
	
	val=val + "+"
	smart_size(val)

def pressed_Minus():
	global val
	
	val=val + "-"
	smart_size(val)

def pressed_Div():
	global val
	
	val=val + "/"
	smart_size(val)
 
def pressed_C():
	global val
	val=""
	smart_size(val)

def pressed_Mul():
	global val
	
	val=val + "*"
	smart_size(val)
	

def pressed_dot():
	global val
	val = val + "."
	smart_size(val)

def pressed_percent():
	global val

	val = val + "%"
	smart_size(val)

	

def pressed_btnB():
	global val
	l = len(val)
	if val[l-4:] in ["cos(", "sin(", "log(", "tan("]:
		val = val[:l-4]
	else:
		val = val[:-1]
	smart_size(val)

def pressed_LB():
	global val
	
	val += "("
	smart_size(val)

def pressed_RB():
	global val
	
	val += ")"
	smart_size(val)

def result():
	global val
	global mode
	# if "π" in val:
	val = re.sub("π", "math.pi", val)
	# if "sin" in val:
	val = re.sub("sin\(", "math.sin(", val)	
	# if "cos" in val:
	val = re.sub("cos\(", "math.cos(", val)		
	# if "tan" in val:
	val = re.sub("tan\(", "math.tan(", val)

	# if "sinh" in val:
	val = re.sub("sinh", "math.sinh", val)	
	# if "cos" in val:
	val = re.sub("cosh", "math.cosh", val)		
	# if "tan" in val:
	val = re.sub("tanh", "math.tanh", val)


	# if "log" in val:
	val = re.sub("log", "math.log", val)
	# if "%" in val:
	val = re.sub("%", "* 0.01", val)
	
	while "!" in val:
		pat = re.compile(r"\d+(?<=)!")
		n = re.search(pat, val)
		str1 = val[n.start():n.end()]
		num = val[n.start():n.end()-1]
		rep = "math.factorial(" + num + ")"
		val = val.replace(str1, rep)

	try:
		val = str(eval(val))
	except Exception as e:
		lbl.configure(fg = "white", bg = "#cc0000")
		messagebox.showerror("Error", e)
		if mode == 0:
			lbl.configure(fg = "black", bg = "#b7b7b7")
		else:
			lbl.configure(fg = "white", bg = "#242424")
	smart_size(val)

def S_X():
	global val

	val += "x"
	smart_size(val)
def S_Y():
	global val

	val += "y"
	smart_size(val)

def S_fact():
	global val

	val += "!"
	smart_size(val)

def S_sin():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	val += "sin("
	
	smart_size(val)

def S_sinh():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	val += "sinh("
	
	smart_size(val)

def S_cos():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	val += "cos("
	smart_size(val)

def S_cosh():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	val += "cosh("
	smart_size(val)

def S_tan():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	val += "tan("

	smart_size(val)

def S_tanh():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	val += "tanh("

	smart_size(val)

def S_log():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	
	val += "log("
	smart_size(val)

def S_pi():
	global operators
	global val

	if val != "" and val[-1] not in operators:
		val += "*"
	val += "π"
	smart_size(val)
	
def S_exp():
	global val
	val += "**"
	smart_size(val)

def donothing():
	pass

def lightmode():
	global mode
	mode = 0
	front = "black"
	back = root["bg"]
	print("light mode enabled")

	lbl.configure(fg = front, bg= "#b7b7b7")
	btnrowS1.configure(bg= "#b7b7b7")
	btnrowS2.configure(bg= "#b7b7b7")
	queryRow.configure(bg = "#b7b7b7" )
	btnSubmit.configure(bg = "#000055")

	btnrow0.configure(bg = back)
	btnS.configure(bg = "#000055")
	btnT.configure(bg = "#000055")
	btnV.configure(bg = "#000055")


	btnLB.configure(fg= front ,bg= back)
	btnRB.configure(fg= front ,bg= back)
	btnMod.configure(fg= front ,bg= back)
	btnDiv.configure(fg= front ,bg= back)
	
	btn7.configure(fg= front ,bg= back)
	btn8.configure(fg= front ,bg= back)
	btn9.configure(fg= front ,bg= back)
	btnMul.configure(fg= front ,bg= back)

	btn4.configure(fg= front ,bg= back)
	btn5.configure(fg= front ,bg= back)
	btn6.configure(fg= front ,bg= back)
	btnMinus.configure(fg= front ,bg= back)
	
	btn1.configure(fg= front ,bg= back)
	btn2.configure(fg= front ,bg= back)
	btn3.configure(fg= front ,bg= back)
	btnPlus.configure(fg= front ,bg= back)

	btn_dot.configure(fg= front ,bg= back)
	btn0.configure(fg= front ,bg= back)
	btn_AC.configure(fg= front ,bg= back)
	btnEq.configure(fg= "sea green" ,bg= back)
	
def darkmode():
	global mode
	mode = 1
	front = "white"
	back = "#242424"
	print("dark mode enabled")

	lbl.configure(fg = front, bg= "#333333")
	btnrowS1.configure(bg= back)
	btnrowS2.configure(bg= back)
	queryRow.configure(bg = back )
	btnSubmit.configure(bg = "green")
 

	btnrow0.configure(bg = back)
	btnS.configure(bg = "green")
	btnT.configure(bg = "green")
	btnV.configure(bg = "green")


	btnLB.configure(fg= front ,bg= back)
	btnRB.configure(fg= front ,bg= back)
	btnMod.configure(fg= front ,bg= back)
	btnDiv.configure(fg= front ,bg= back)
	
	btn7.configure(fg= front ,bg= back)
	btn8.configure(fg= front ,bg= back)
	btn9.configure(fg= front ,bg= back)
	btnMul.configure(fg= front ,bg= back)

	btn4.configure(fg= front ,bg= back)
	btn5.configure(fg= front ,bg= back)
	btn6.configure(fg= front ,bg= back)
	btnMinus.configure(fg= front ,bg= back)
	
	btn1.configure(fg= front ,bg= back)
	btn2.configure(fg= front ,bg= back)
	btn3.configure(fg= front ,bg= back)
	btnPlus.configure(fg= front ,bg= back)

	btn_dot.configure(fg= front ,bg= back)
	btn0.configure(fg= front ,bg= back)
	btn_AC.configure(fg= front ,bg= back)
	btnEq.configure(fg= front ,bg= back)


root= tk.Tk()
root.geometry("400x600+800+25")
root.resizable(0,0)
root.title("Calculator")

menubar = Menu(root)

Modemenu = Menu(menubar, tearoff = 0,)
Modemenu.add_command(label="Light", command=lightmode)
Modemenu.add_command(label="Dark", command=darkmode)
menubar.add_cascade(label="Mode", menu=Modemenu)



editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
# editmenu.add_command(label="Mode", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)





data = StringVar()
lbl=Label(root,height = "3",justify = "right",textvariable=data,font=("Verdana",18),anchor=SE,bg="#b7b7b7")
lbl.pack(expand=True,fill="both",)

scientific = 0
query_enable = 0

def query_type():
	global queryRow
	global btnSubmit
	global query_enable
	global mode

	if query_enable == 0:
		query_enable = 1

		if mode == 0:
			queryRow = Frame(root, bg="#b7b7b7" )
			Entry1 = tk.Entry(queryRow, textvariable = 1,)
			Entry1.pack(side= LEFT,padx = 10,pady = 7,ipadx = 85,ipady = 5)

			def get():
				query_text = Entry1.get()
				search(query_text)

			btnSubmit=Button(queryRow,text="Submit",font=("Verdana",12),border=0,relief=GROOVE,fg = "white" ,bg = "#000055", command = get)
			btnSubmit.pack(side = LEFT,expand=True,)
		else:
			queryRow = Frame(root, bg="#242424" )
			Entry1 = tk.Entry(queryRow, textvariable = 1,)
			Entry1.pack(side= LEFT,padx = 10,ipadx = 85,ipady = 5)

			def get():
				query_text = Entry1.get()
				search(query_text)

			
			btnSubmit=Button(queryRow,text="Submit",font=("Verdana",12),border=0,relief=GROOVE,fg = "white" ,bg = "green", command = get)
			btnSubmit.pack(side = LEFT,expand=True,)
		queryRow.pack(expand=True, fill ="both",)


	else:
		query_enable = 0
		queryRow.destroy()
		queryRow = Frame(root)
		
	

def scie():
	global scientific
	global btnrowS1
	global btnrowS2
	global mode

	if scientific == 0:
		scientific = 1
		print(mode)
		if mode == 1:
			back = root["bg"]
			front = "black"
			btnrowS1 = Frame(root, bg="#242424" )
			btnrowS2 = Frame(root, bg="#242424" )
			btnSin=Button(btnrowS1,text=" sin ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_sin)
			btnSin.pack(side = LEFT,expand=True,)
			btnCos=Button(btnrowS1,text=" cos ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_cos)
			btnCos.pack(side = LEFT,expand=True,)
			btnTan=Button(btnrowS1,text=" tan ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_tan)
			btnTan.pack(side = LEFT,expand=True,)
			btnPi=Button(btnrowS1,text=" π ",font=("Arial",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_pi)
			btnPi.pack(side = LEFT,expand=True,)
			btnFact=Button(btnrowS1,text=" n!",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_fact)
			btnFact.pack(side = LEFT,expand=True,)
			btnLog=Button(btnrowS1,text="log",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_log)
			btnLog.pack(side = LEFT,expand=True,)

			btnSinh=Button(btnrowS2,text="sinh",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_sinh)
			btnSinh.pack(side = LEFT,expand=True,)
			btnCosh=Button(btnrowS2,text="cosh ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_cosh)
			btnCosh.pack(side = LEFT,expand=True,)
			btnTanh=Button(btnrowS2,text="tanh",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_tanh)
			btnTanh.pack(side = LEFT,expand=True,)
			btnX=Button(btnrowS2,text=" x ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_X)
			btnX.pack(side = LEFT,expand=True,)
			btnY=Button(btnrowS2,text=" y ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_Y)
			btnY.pack(side = LEFT,expand=True,)
			btnExp=Button(btnrowS2,text="Exp",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_exp)
			btnExp.pack(side = LEFT,expand=True,)

		else:
			front = "#121212"	
			back = "dark grey"
			btnrowS1 = Frame(root, bg="#242424" )
			btnrowS2 = Frame(root, bg="#242424" )
			btnSin=Button(btnrowS1,text=" sin ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_sin)
			btnSin.pack(side = LEFT,expand=True,)
			btnCos=Button(btnrowS1,text=" cos ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_cos)
			btnCos.pack(side = LEFT,expand=True,)
			btnTan=Button(btnrowS1,text=" tan ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_tan)
			btnTan.pack(side = LEFT,expand=True,)
			btnPi=Button(btnrowS1,text=" π ",font=("Arial",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_pi)
			btnPi.pack(side = LEFT,expand=True,)
			btnFact=Button(btnrowS1,text=" n!",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_fact)
			btnFact.pack(side = LEFT,expand=True,)
			btnLog=Button(btnrowS1,text="log",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_log)
			btnLog.pack(side = LEFT,expand=True,)

			btnSinh=Button(btnrowS2,text="sinh",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_sinh)
			btnSinh.pack(side = LEFT,expand=True,)
			btnCosh=Button(btnrowS2,text="cosh ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_cosh)
			btnCosh.pack(side = LEFT,expand=True,)
			btnTanh=Button(btnrowS2,text="tanh",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_tanh)
			btnTanh.pack(side = LEFT,expand=True,)
			btnX=Button(btnrowS2,text=" x ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_X)
			btnX.pack(side = LEFT,expand=True,)
			btnY=Button(btnrowS2,text=" y ",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_Y)
			btnY.pack(side = LEFT,expand=True,)
			btnExp=Button(btnrowS2,text="Exp",font=("Verdana",12),border=0,relief=GROOVE, fg = front, bg = back, command = S_exp)
			btnExp.pack(side = LEFT,expand=True,)

		btnrowS1.pack(expand=True, fill ="both",)
		btnrowS2.pack(expand=True, fill ="both",)

		
	else:
		scientific = 0
		btnrowS1.destroy()
		btnrowS2.destroy()
		btnrowS2 = Frame(root)
		btnrowS1 = Frame(root)


btnrow0 = Frame(root)
btnrow0.pack(expand=True, fill ="both",)
btnS=Button(btnrow0,text="Scie",font=("Verdana",12),border=0,fg = "white" ,bg = "#000055",relief=GROOVE,command = scie)
btnS.pack(side = LEFT,expand=True,)

btnV=Button(btnrow0,text="Voice",font=("Verdana",12),border=0,fg = "white" ,bg = "#000055",relief=GROOVE, command = pressed_btnV)
btnV.pack(side = LEFT,expand=True,)

btnT=Button(btnrow0,text="Type",font=("Verdana",12),border=0,fg = "white" ,bg = "#000055",relief=GROOVE, command = query_type)
btnT.pack(side = LEFT,expand=True,)


btnB=Button(btnrow0,text="<--",font=("Verdana",12),border=0,fg = "white" ,bg = "dark red",relief=GROOVE,command = pressed_btnB)
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
btnrowS2 = Frame()
queryRow = Frame()
btnSubmit = Button()


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