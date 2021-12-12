import tkinter
from tkinter import *
import shutil 
import easygui





window = tkinter.Tk()
window.geometry('550x350')

def openWelcomeWindow():
	WelcomeWindow = Toplevel(window)
	WelcomeWindow.title("It's welcome page")
	WelcomeWindow.geometry('300x300')
	Label(WelcomeWindow, text = " Тавтай морилно уу").pack()
	#info_dms = tkinter.
	Label(WelcomeWindow, text = "\n\nЭнэхүү програм нь таны DMS \nфайлуудыг автоматаар хуулах зориулалттай.").pack()
	author_pos = tkinter.Label(WelcomeWindow, text = "Author : Эрдэнэтогтох")#.pack()
	author_pos.place(relx = 0.0,
		        	 rely = 1.0,
		        	 anchor = 'sw')


def Omni():
	
	
	#source =  file
	dest =  "D:/DMS project dest/Omni/result.txt"
	try:
		file = easygui.fileopenbox()
		source = file
		shutil.copy(source, dest)
		#print("File copied successfully.")
		success = Toplevel(window)
		success.geometry('300x50')
		success.title('Програмын үр дүн')
		#Label(success, text = 'Амжилттай!', fill='green').pack()
		canvar = Canvas(success, width = 300, height = 100, bg='white')
		canvar.create_text(150, 0, text = '\n\nАмжилттай хууллаа!', fill = 'green', font = ('Helvetica 18'))
		canvar.pack()

	except shutil.SameFileError:
		print("Source and destination represents the same file.")

	except PermissionError:
		print('permission denied')
		perm_deny = Toplevel(window)
		perm_deny.geometry('500x500')
		perm_deny.title('Permissin Denied!')
		permD = Canvas(success, width = 300, height = 100, bg='red')
		permD.create_text(150, 0, text = '\nТаны эрх хүрэхгүй байна.!', fill = 'red', font = ('Helvetica 15'))
	except:
		helpDisk = Toplevel(window)
		helpDisk.geometry('300x300')
		helpCanvas = Canvas(success, width = 300, height = 100, bg='white')	
		helpCanvas.create_text(150, 0, text = '\nЭрдэнэтогтох-той холбогдоно уу!', fill = 'black', font = ('Helvetica 15'))
		helpCanvas.pack()
# to rename the title of the window
#window.title("FIRST TIME GUI APP")
#window.title1.place()

window.title("DMS темплейт updater")

canvas = Canvas(window, width = 1000, height = 750, bg='white')
canvas.create_text(180, 10, text = 'Сайн байна уу? Та хийх үйлдэлээ сонгоно уу.', fill = 'red', font = ('Helvetica 12'))
canvas.pack()

#canvas.create_text(100, 40, text = '\n1. DMS file upload to server', fill = 'green', font = ('Helvetica 10 bold'))
server_button = tkinter.Button(window, text = '1. Upload DMS file to server' )
server_button.place(relx = 0.30,
				    rely = 0.15,
				    anchor = 'ne')


#canvas.create_text(145, 80, text = "2. DMS file upload to \\192.168.205.15\Omni", 192.168.205.1fill = 'green', font = ('Helvetica 10 bold'))
omni_button = tkinter.Button(window, text = '2. Upload DMS file to \\192.168.205.15\Omni' ,command = Omni)
omni_button.place(relx = 0.45,
				    rely = 0.35,
				    anchor = 'ne')
# \\192.168.205.15\Omni ruu update hiih code



#canvas.create_text(147, 110, text = "3. DMS file upload to \\192.168.205.15\Install", fill = 'green', font = ('Helvetica 10 bold'))
install_button = tkinter.Button(window, text = '3. Upload DMS file to \\192.168.205.15\Install' )
install_button.place(relx = 0.45,
				    rely = 0.55,
				    anchor = 'ne')
# pack is used to show the object in the window
Lower_left = tkinter.Label(window, text = "Lower Left!")#.pack()
Lower_left.place(relx = 0.0,
				 rely = 1.0,
				 anchor = 'ne')

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

author_pos = tkinter.Label(window, text = "Author : Эрдэнэтогтох")#.pack()
author_pos.place(relx = 0.4,
		        	 rely = 1.0,
		        	 anchor = 'sw')
#Button_exit
#button_widget.pack()
window.mainloop()
