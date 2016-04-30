from Tkinter import *
import random

class processFrame(Frame):
	def __init__(self):
		self.parent = Tk()
		self.parent.title("Process Management Algorithms")
		self.parent.geometry("800x400+300+300")
		Frame.__init__(self, self.parent)
		self.grid()


		self.initUI();
		#self.initRoundRobin();
		self.parent.mainloop()

	def printSelection(self):
		print(self.timeQuantaBox.get())

	def generateProcessesList(self):
		random.seed()
		#remove all elelments in the list
		self.processListBox.delete(0, END)
		for i in range(0, int(self.processCountBox.get())): #maybe check that there is actually a number here
			processName = "P" + str(i+1) + ":  " + str(random.randint(0,50)).zfill(2) + "  " + str(random.randint(1,9)) + "  " + str(i+1).zfill(2)
			self.processListBox.insert(END, processName)

	def initUI(self):
		# FRAME FOR PROCESS LIST ON THE LEFT SIDE OF THE WINDOW
		# set up left side column for processes
		self.processListColumnFrame = Frame(self, width=200, height=400, background="grey")
		self.processListColumnFrame.grid_propagate(False);
		self.processListColumnFrame.grid(row=0, column=0)

		# process list
		# show label and entry box for process count
		#self.processCount = 0
		Label(self.processListColumnFrame, text="Enter process count: ").grid(row=0, column=0, sticky=W)
		self.processCountBox = Entry(self.processListColumnFrame)
		self.processCountBox.grid(row=1, column=0, sticky=W)

		# show button for generating process list
		Button(self.processListColumnFrame, text="Generate Process List", command=self.generateProcessesList).grid(row=2, column=0, sticky=W)

		# show label for list box
		Label(self.processListColumnFrame, text="P, Burst t, Priority t, Arrival t").grid(row=3, column=0, sticky=W)

		# show list box for showing the processes
		self.processListBox = Listbox(self.processListColumnFrame)
		self.processListBox.grid(row=4, column=0, sticky=W)

		# END PROCESS COLUMN SUTFF

		# FRAME FOR BUTTONS AND CHART ON THE RIGHT SIDE OF THE WINDOW
		# set up frame for rght side for buttons and process rectangles
		self.dataColumnFrame = Frame(self, width=600, height=400)
		self.dataColumnFrame.grid_propagate(False);
		self.dataColumnFrame.grid(row=0, column=1)

		# FRAME INSIDE OF THE DISPLAY FRAME
		# set up frame for radio buttons and text entry
		self.frameRadioButtons = Frame(self.dataColumnFrame, width=600, height=75)
		self.frameRadioButtons.grid_propagate(False);
		self.frameRadioButtons.grid(sticky=W,row=0, column=0)

		# variable for getting a number based on radio button choosen
		self.selectedMethod = IntVar(master=self.parent)

		# set up round robin radio button
		self.roundRobinButton = Radiobutton(self.frameRadioButtons, command=self.printSelection, text="Round Robin", variable=self.selectedMethod, value=0)
		self.roundRobinButton.grid(sticky=N, row=0, column=0)

		# set up priority button (scheduling)
		self.priorityButton = Radiobutton(self.frameRadioButtons, command=self.printSelection, text="Priority", variable=self.selectedMethod, value=1)
		self.priorityButton.grid(sticky=N, row=0, column=1)

		# set up shortest job first button
		self.shortestJobFirstButton = Radiobutton(self.frameRadioButtons, command=self.printSelection, text="Shortest Job First", variable=self.selectedMethod, value=2)
		self.shortestJobFirstButton.grid(sticky=N, row=0, column=2)

		# default radio button to be selected
		self.roundRobinButton.select()

		# set up frame for where the processes are going to be visually displayed
		self.processDisplay = Frame(self.dataColumnFrame, width=600, height=325)
		self.processDisplay.grid_propagate(False);
		self.processDisplay.grid(row=1, column=0)

		# label and entry for the time quanta - only for round robin
		self.timeQuanta = StringVar()
		Label(self.frameRadioButtons, text="Time Quanta (Round Robin only): ").grid(row=1, column=0)
		self.timeQuantaBox = Entry(self.frameRadioButtons)
		self.timeQuantaBox.grid(row=1, column=1)

		# button for generating the process display
		Button(self.frameRadioButtons, text="Generate", command=self.processLoop).grid(row=1, column=2)

	# def initRoundRobin(self):
	# 	self.roundRobinFrame = Frame(self)
	# 	self.roundRobinFrame.grid(row = 1, column = 2)
	# 	self.timeQuanta = StringVar()
	#
	# 	Label(self.roundRobinFrame, text="Time Quanta: ").grid(row = 0, column =  0)
	# 	self.timeQuantaBox = Entry(self.roundRobinFrame)
	# 	self.timeQuantaBox.grid(row = 0, column = 1)



	def processLoop(self):
		print("Generating...")
		processName = []
		processList = []
		for i in range(0, 5):
			can = Canvas(self.processDisplay, width=50, height=50)
			processList.append(can)
			processList[i].create_rectangle(0, 0, 50, 50, fill="blue")
			processList[i].grid(row=0, column=i)
