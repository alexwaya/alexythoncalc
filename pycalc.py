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
		ENtry(self, relief=FLAT,
			textvariable = display, justify ="right", bd=30, bg="powder blue".pack(side=TOP, expand=YES, fill=BOTH))


		for clearBut in xrange(["CE"], ["C"]):
			erase = iCalc(self,TOP)
			for ichar in clearBut:
				button(erase,LEFT,ichar,
					lambda storeObj=display, q=ichar: storeObj.set(""))
			
		for NumBut in ("789/", "456*", "123-", "0.+"):
			FunctionNum = iCalc(self, TOP)
			for char in NumBut:
				button(FunctionNum, LEFT, char,
					lambda storeObj=display, q=char: storeObj.get() + q)
			


		