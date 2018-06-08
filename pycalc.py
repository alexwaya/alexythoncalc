from tkinter import*


def iCalc(source, side):
	storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
	storeObj.pack(side=side, expand=YES, fill=BOTH)
	return storeObj

def button(source, side, text, command=None):
	storeObj = Button(source, text=text, command=command)
	storeObj.pack(side=side, expand=YES, fill=BOTH)
	return storeObj

#class declaration
class app(Frame):
	#docstring fos app
	def __init__(self):
		#supes app, self).__init__()
		Frame.__init__(self)
		self.option_add = ("*Font", "arial 20 bold")
		self.pack(expand=YES, fill=BOTH)
		self.master.title("Alexython Calculator")

		display = StringVar('')
		dispwc = Entry(self, relief=RIDGE,textvariable = display, justify ="right", bd=30, bg="powder blue")
		dispwc.pack(side=TOP, expand=YES, fill=BOTH)


		for clearBut in (["CE"], ["C"]):
			erase = iCalc(self,TOP)
			for iEquals in clearBut:
				button(erase,LEFT,iEquals,
					lambda storeObj=display, q=iEquals: storeObj.set(""))
		#Adding Text Units	

		
		for NumBut in ("789/", "456*", "123-", "0.+"):
			FunctionNum = iCalc(self, TOP)
			for iEquals in NumBut:
				button(FunctionNum, LEFT, iEquals,
					lambda storeObj=display, q=iEquals: storeObj.get() + q)

		#Equal Button for calculations
		EqualsButton = iCalc(self, TOP)
		for iEquals in "=":
			if iEquals == "=":
				btniEquals = button(EqualsButton, LEFT, iEquals)
				btniEquals.bind("ButtonRelease-1",
					lambda e, s=self, storeObj=display: s.calc(storeObj), "+")

			else:
				btniEquals = button(EqualsButton, LEFT, iEquals,
					lambda storeObj=display, s="%s " %iEquals: storeObj.set(storeObj.get()+s))
			

		#Error Handling
		def calc(self, display):
			try:
				display.set(eval(display.get()))
			except:
				display.set("ERROR")


#Initialize this App
if __name__ == '__main__':
	app().mainloop()