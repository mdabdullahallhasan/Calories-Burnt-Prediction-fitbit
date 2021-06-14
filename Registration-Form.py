# Task:
# After Filling details in Form and Clicking on 
# Submit button, the records (Text)  will be saved on a file
# named as user.txt and it will contain all user entered details. If file is not created,
# then automatically it will Create.
# Email Verification, Field Required will be take care in this Form.
# Reset Button Will erase all data in Text area fileds.
# Registration form bcz it covers almost everything such as label, entry field, radio buttton
# Checkbox, submit button, icon, font face, font size, bold, italic, underline etc etc

import re
from tkinter import *
import tkinter as tk
regex = '^\w([\.-]?\w+)*@\w([\.-]?\w+)*(\.\w{2,3})+$'

def filedreq():
	if Fname.get() == "":
		print("First Name Field is Empty!!")
		user = "First Name Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=580)


	elif Lname.get() == "":
		print("Last Name Field is Empty!!")
		user = "Last Name Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=580)

	elif Email.get() == "":
		print("Email Field is Empty!!")
		user = "Email Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=580)

	elif Password.get() == "":
		print("Password Field is Empty!!")
		user = "Password Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=580)

	elif entry_Address.compare("end-1c", "==", "1.0"):     # or else  if len(text.get("1.0", "end-1c")) == 0:
		print("Address Field is Empty!!")
		user = "Address Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=580)

	else:
		checkemail()

def checkemail():
	email = Email.get()

	if(re.search(regex,email)):
		print("Valid Email")
		user = "Valid Email!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=580)
		save()

	else:
		print("Invalid Email!!")
		user = "Invalid Email-Type!! Type Correct Mail: Format: xyz@abc.com"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=580)

def save():
	First = Fname.get()
	Last = Lname.get()
	email = Email.get()
	address = entry_Address.get(1.0,END)
	password = Password.get()
	gender = str(radio.get())  
	php = check.get()
	java = check2.get()
	nt = check3.get()
	py = check4.get()
	dep = variable.get()

	if php =='1':
		php ="PHP"
	if java =='1':
		java ="JAVA"
	if nt =='1':
		nt =".NET"
	if py =='1':
		py ="PYTHON"
	file = open("user.txt","a")
	file.write("\n\nFirst Name: "+First+"\n")
	file.write("Last Name: "+Last+"\n")
	file.write("Password: "+password+"\n")
	file.write("Email: "+email+"\n")
	file.write("Address "+address)
	file.write("Gender: "+gender+"\n")
	file.write("Course: ")
	file.write(php+" ")
	file.write(nt+" ")
	file.write(java+" ")
	file.write(py+" ")
	file.write("\nDepartment: "+dep+" ")
	file.close()
	user = First + " has successfully Registered and Record is saved in user.txt file"
	Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=580)
	print("Printing Data: ")
	print(First,Last,password,email,address,gender,php,java,nt,py)

def reset():
	Fname.set("")
	Lname.set("")
	Email.set("")
	Password.set("")
	entry_Address.delete(1.0,END)
	#
	#
	#
	#



win =  Tk()

win.geometry("400x600")
win.configure(background="cyan")
win.title("Registration Form")
win.iconbitmap('icon.ico')


title = Label(win, text="Registration Form", bg="gray", width="300", height="2", fg="white", font = ("Calibri 20 bold italic underline")).pack()

Fname = Label(win, text="First Name: ", bg="cyan", font=("Verdana 12")).place(x=12, y=100)

Lname = Label(win, text="Last Name: ", bg="cyan", font=("Verdana 12")).place(x=12, y=140)

email = Label(win, text="Email: ", bg="cyan", font=("Verdana 12")).place(x=12, y=180)

Password = Label(win, text="Password: ", bg="cyan", font=("Verdana 12")).place(x=12, y=220)

Address = Label(win, text="Address: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=260)

Gender = Label(win, text="Gender: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=300)

radio = StringVar()
Male = Radiobutton(win, text="Male",bg="cyan",variable=radio,value="Male",font = ("Verdana 12")).place(x=12,y=340)
Female = Radiobutton(win, text="Female",bg="cyan",variable=radio,value="Female",font = ("Verdana 12")).place(x=120,y=340)

AC = Label(win,text="Applied Course: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=380)
check = StringVar()
check2 = StringVar()
check3= StringVar()
check4 = StringVar()

PHP = Checkbutton(win, text = "PHP",variable=check,bg="cyan",font = ("Verdana 12")).place(x=12,y=420)
Java = Checkbutton(win, text = "Java",bg="cyan",variable=check2,font = ("Verdana 12")).place(x=120,y=420)
net = Checkbutton(win, text = ".net",bg="cyan",variable=check3,font = ("Verdana 12")).place(x=12,y=460)
Python = Checkbutton(win, text = "Python",bg="cyan",variable=check4,font = ("Verdana 12")).place(x=120,y=460)


dept = Label(win,text="Department: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=500)
variable = StringVar(win)
variable.set("Dept: ")
w = OptionMenu(win, variable, "CSE", "IT", "CS")
w.place(x=140,y=500)


Fname = StringVar()
Lname = StringVar()
Email = StringVar()
Password = StringVar()
Address  = StringVar()
Gender = StringVar()
Courses  = StringVar()

entry_Fname = Entry(win,textvariable = Fname,width=30)
entry_Fname.place(x=120,y=100)

entry_Lname = Entry(win,textvariable = Lname,width=30)
entry_Lname.place(x=120,y=140)

entry_email = Entry(win,textvariable = Email,width=30)
entry_email.place(x=120,y=180)

entry_password = Entry(win, show="*",textvariable = Password,width=30)
entry_password.place(x=120,y=220)

entry_Address = Text(win,height=2,width=23)
entry_Address.place(x=119,y=260)

reset = Button(win, text="Reset", width="12",height="1",activebackground="red",command=reset, bg="Pink",font = ("Calibri 12 ")).place(x=24, y=540)
submit = Button(win, text="Submit", width="12",height="1",activebackground="violet", bg="Pink",command=filedreq,font = ("Calibri 12 ")).place(x=240, y=540)


win.mainloop()
	
