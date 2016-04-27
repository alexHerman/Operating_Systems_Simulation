from tkinter import *

class memoryFrame(Frame):
	def __init__(self):
		parent = Tk()
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Process Management Algorithms")
		self.pack()
		self.mainloop()
