import tkinter
from tkinter import *

window = tkinter.Tk()
window.geometry('550x350')

def openWelcomeWindow():
	WelcomeWindow = Toplevel(window)
	WelcomeWindow.title("It's welcome page")
	WelcomeWindow.geometry('300x300')
	Label(WelcomeWindow, text = " Тавтай морилно уу").pack()
	Label(WelcomeWindow, text = "\n\nЭнэхүү програм нь таны DMS \nфайлуудыг автоматаар хуулах зориулалттай.").pack()
	Bottom = tkinter.Label(WelcomeWindow, text = "Author : Эрдэнэтогтох")#.pack()
	Bottom.place(reLx = 0.5,
		         rely = 0.5,
		         anchor = 'center')


# to rename the title of the window
window.title("FIRST TIME GUI APP")
#window.title1.place()

window.title("DMS темплейт updater")

canvas = Canvas(window, width = 1000, height = 750, bg='white')
canvas.create_text(160, 10, text = 'Сайн байна уу? Та хийх үйлдэлээ сонгоно уу.', fill = 'red', font = ('Helvetica 11'))
canvas.pack()

canvas.create_text(100, 40, text = '1. DMS file upload to server', fill = 'green', font = ('Helvetica 10 bold'))
# pack is used to show the object in the window
Lower_left = tkinter.Label(window, text = "Lower Left!")#.pack()
Lower_left.place(relx = 0.0,
				 rely = 1.0,
				 anchor = 'sw')

#Welcome_button = tkinter.Button(window, text='\nWelcome',command = openWelcomeWindow).pack()#,command = openWelcomeWindow.pack() #,command = openWelcomeWindow
Welcome_button = tkinter.Button(window, text='Мэдээлэл' ,command = openWelcomeWindow)
Welcome_button.place(relx = 0.0,
			         rely = 1.0, 
			         anchor = 'sw')
#button_widget.pack()

Button_exit = tkinter.Button(window, text = 'Exit!' ,command = window.destroy)#.pack()
Button_exit.place(relx = 1.0,
				  rely = 1.0,
				  anchor = 'se')  #n, ne, e, se, s, sw, w, nw, or center
#Button_exit
#button_widget.pack()
window.mainloop()
