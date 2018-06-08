from tkinter import*

def iCalc(source, side):
	storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
	storeObj.pack(side=side, expand=YES, fill=BOTH)
	return storeObj

def button(source, side, text, command=None):
	storeObj = Button(source, text=text, command=command)
	storeObj.pack(side=side, expand=YES, fill=BOTH)
	return storeObj

class app(Frame):
	"""docstring fos app"""
	def __init__(self, arg):
		#supes app, self).__init__()
		Frame.__init__(self)
		self.option_add = ("*Font", "arial 20 bold")
		self.pack(expand=YES, fill=BOTH)
		self.master.title("Calculator")

		display = StringVar()
		ENtry(self, relief=,
			)


		