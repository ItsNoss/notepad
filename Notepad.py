import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title('Notepad')

def new():
	root.title('Notepad - New File')
	text.delete(1.0, END)

def openFile():
	file = filedialog.askopenfilename(parent=root, title='Select File', filetypes=(('text files', '*.txt'), ('all files', '*.*')))
	root.title(file)
	with open(file, 'r') as of:
		contents = of.read()
		text.insert(1.0, contents)

def saveAs():
	file = filedialog.asksaveasfilename(title='Save File', filetypes=(('text files', '*.txt'), ('python files', '*.py'), ('all files', '*.*')))
	with open(file+'.txt', 'w') as sf:
		output = text.get(1.0, END)
		sf.write(output)

def cut():
        pass

def about():
	messagebox.showinfo(message='Lick my toes')

class windowSize():
	def __init__(self, master):
		master.minsize(width=500, height=400)

w = windowSize(root)

# Text box and scroll bar
text = Text(root)
text.pack(side=LEFT, fill=BOTH, expand=YES)
s = Scrollbar(root, command=text.yview)
s.pack(side=RIGHT, fill=Y)
text.configure(yscrollcommand=s.set, undo=True)

# Menu Bar
menubar = Menu(root)
root['menu'] = menubar

menu_file = Menu(menubar, tearoff=0)
menubar.add_cascade(menu=menu_file, label='File')
menu_file.add_command(label='New', command=new)
menu_file.add_command(label='Open', command=openFile)
menu_file.add_command(label='Save')
menu_file.add_command(label='Save As', command=saveAs)

menu_edit = Menu(menubar, tearoff=0)
menubar.add_cascade(menu=menu_edit, label='Edit')
menu_edit.add_command(label='Cut Ctrl+x', command=cut)
menu_edit.add_command(label='Copy')
menu_edit.add_command(label='Paste')


menu_help = Menu(menubar, tearoff=0)
menubar.add_cascade(menu=menu_help, label="Help")
menu_help.add_command(label='About', command=about)

root.mainloop()