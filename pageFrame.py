from tkinter import *

class pageFrame(Frame):
	def __init__(self):
		parent = Tk()
    	parent.geometry("250x150+300+300")
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()
		parent.mainloop()

	def initUI(self):
		self.parent.title("Process Management Algorithms")
		self.pack()

		frameLeft = Frame(self, background="green")
		frameRight = Frame(self)
		frameLeft.pack(fill=X)
		frameRight.pack(fill=X)
