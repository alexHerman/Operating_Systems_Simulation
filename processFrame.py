from tkinter import *


class processFrame(Frame):
	def __init__(self):
		self.parent = Tk()
		self.parent.title("Process Management Algorithms")
		self.parent.geometry("500x300+300+300")
		Frame.__init__(self, self.parent)
		self.pack(fill=BOTH, expand=1)

		self.selectedMethod = IntVar(master = self.parent)
		self.initUI();
		self.parent.mainloop()

	def printSelection(self):
		print(self.selectedMethod.get())

	def initUI(self):
		frameRadioButtons = Frame(self)
		frameRadioButtons.grid(row = 0)

		roundRobinButton = Radiobutton(frameRadioButtons, command=self.printSelection, text = "Round Robin", variable = self.selectedMethod, value = 0)
		roundRobinButton.grid(row = 0, column = 0)
		priorityButton = Radiobutton(frameRadioButtons, command=self.printSelection, text = "Priority", variable = self.selectedMethod, value = 1).grid(row = 0, column = 1)
		shortestJobFirstButton = Radiobutton(frameRadioButtons, command=self.printSelection, text = "Shortest Job First", variable = self.selectedMethod, value = 2).grid(row = 0, column = 2)
		roundRobinButton.select()

		frameRadioButtons.pack(fill=BOTH)
