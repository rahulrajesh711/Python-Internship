from tkinter import *
from tkinter import *
from tkinter.messagebox import *
import requests
import bs4

#QOTD code
try:
	url = ""
except Exception as e:
	print("issue ",e)

#main window/ems window
emsWindow = Tk()      
emsWindow.title("E.M.S")
emsWindow['background'] = '#b3ffc6'
emsWindow.geometry("420x500+100+100")
f = ("Ariel",10,"bold")

def addWindow():
	emsWindow.destroy()
	addWindow = Tk()
	addWindow.title("Add Employee")
	addWindow['background'] = '#b3ecff'
	addWindow.geometry("420x500+100+100")
	f = ("Ariel",10,"bold")

def viewEmpWindow():
	emsWindow.destroy()
	viewEmpWindow = Tk()
	viewEmpWindow.title("View Employee")
	viewEmpWindow['background'] = '#ffff99'
	viewEmpWindow.geometry("420x500+100+100")
	f = ("Ariel",10,"bold")

def updEmpWindow():
	emsWindow.destroy()
	updEmpWindow = Tk()
	updEmpWindow.title("Update Employee")
	updEmpWindow['background'] = '#ffc6b3'
	updEmpWindow.geometry("420x500+100+100")
	f = ("Ariel",10,"bold")

def delEmpWindow():
	emsWindow.destroy()
	delEmpWindow = Tk()
	delEmpWindow.title("Delete Employee")
	delEmpWindow['background'] = '#80dfff'
	delEmpWindow.geometry("420x500+100+100")
	f = ("Ariel",10,"bold")

#button assignments
btn_add = Button(emsWindow,text="Add",font = f,width=25,command = addWindow)
btn_view = Button(emsWindow,text="View",font = f,width=25,command = viewEmpWindow)
btn_update = Button(emsWindow,text="Update",font = f,width=25,command = updEmpWindow)
btn_delete = Button(emsWindow,text="Delete",font = f,width=25,command = delEmpWindow)
btn_charts = Button(emsWindow,text="Charts",font = f,width=25)

# button placement for main ems window
btn_add.place(x=110,y=50)
btn_view.place(x=110,y=90)
btn_update.place(x=110,y=130)
btn_delete.place(x=110,y=170)
btn_charts.place(x=110,y=210)

#label assignments
nf = ("Ariel",20)
label_QOTD = Label(emsWindow,text="QOTD:\n",font = nf)

#label placement for main ems window
label_QOTD.place(x=0,y=300)

emsWindow.mainloop()
