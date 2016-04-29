from tkinter import *

class processFrame(Frame):
	def __init__(self):
		self.parent = Tk()
		self.parent.title("Process Management Algorithms")
		self.parent.geometry("500x300+300+300")
		Frame.__init__(self, self.parent)
		self.grid()

		self.initUI();
		self.initRoundRobin();
		self.parent.mainloop()

	def printSelection(self):
		print(self.timeQuantaBox.get())

	def initUI(self):
		frameRadioButtons = Frame(self)
		frameRadioButtons.grid(row = 0)

		self.selectedMethod = IntVar(master = self.parent)
		roundRobinButton = Radiobutton(frameRadioButtons, command=self.printSelection, text = "Round Robin", variable = self.selectedMethod, value = 0)
		roundRobinButton.grid(row = 0, column = 0)
		priorityButton = Radiobutton(frameRadioButtons, command=self.printSelection, text = "Priority", variable = self.selectedMethod, value = 1).grid(row = 0, column = 1)
		shortestJobFirstButton = Radiobutton(frameRadioButtons, command=self.printSelection, text = "Shortest Job First", variable = self.selectedMethod, value = 2).grid(row = 0, column = 2)
		roundRobinButton.select()

	def initRoundRobin(self):
		self.roundRobinFrame = Frame(self)
		self.roundRobinFrame.grid(row = 1, column = 0)
		self.timeQuanta = StringVar()

		Label(self.roundRobinFrame, text="Time Quanta: ").grid(row = 0, column =  0)
		self.timeQuantaBox = Entry(self.roundRobinFrame)
		self.timeQuantaBox.grid(row = 0, column = 1)
