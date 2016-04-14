from tkinter import *

class processFrame(Frame):
	def __init__(self):
		parent = Tk()
		parent.geometry("250x150+300+300")
		Frame.__init__(self, parent)
		self.parent = parent
		self.initUI()
		parent.mainloop()

	def initUI(self):
		self.parent.title("Process Management Algorithms")
		self.pack(fill=BOTH, expand=1)

		frameLeft = Frame(self, background="green")
		frameRight = Frame(self, background="red")
		frameLeft.pack(fill=X)
		frameRight.pack(fill=X)
