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

	def sortProcessesByPriority(self):
		sizeOfList = int(self.processCountBox.get())
		for i in range(sizeOfList-1, 0, -1):
			for j in range(i):
				if self.processPrioriy[j] > self.processPrioriy[j+1]:
					# swap process priorities
					swap = self.processPrioriy[j]
					self.processPrioriy[j] = self.processPrioriy[j+1]
					self.processPrioriy[j+1] = swap
					# swap process burst times
					swap = self.processBurstTime[j]
					self.processBurstTime[j] = self.processBurstTime[j+1]
					self.processBurstTime[j+1] = swap
					# swap process name
					swap = self.processName[j]
					self.processName[j] = self.processName[j+1]
					self.processName[j+1] = swap
					# swap process arrival time
					swap = self.processArrival[j]
					self.processArrival[j] = self.processArrival[j+1]
					self.processArrival[j+1] = swap

	def sortProcessesByBurstTime(self):
		sizeOfList = int(self.processCountBox.get())
		for i in range(sizeOfList-1, 0, -1):
			for j in range(i):
				if self.processBurstTime[j] > self.processBurstTime[j+1]:
					# swap process burst times
					swap = self.processBurstTime[j]
					self.processBurstTime[j] = self.processBurstTime[j+1]
					self.processBurstTime[j+1] = swap
					# swap process priorities
					swap = self.processPrioriy[j]
					self.processPrioriy[j] = self.processPrioriy[j+1]
					self.processPrioriy[j+1] = swap
					# swap process name
					swap = self.processName[j]
					self.processName[j] = self.processName[j+1]
					self.processName[j+1] = swap
					# swap process arrival time
					swap = self.processArrival[j]
					self.processArrival[j] = self.processArrival[j+1]
					self.processArrival[j+1] = swap

	def sortProcessesByArrivalTime(self):
		sizeOfList = int(self.processCountBox.get())
		for i in range(sizeOfList-1, 0, -1):
			for j in range(i):
				if self.processArrival[j] > self.processArrival[j+1]:
					# swap process arrival time
					swap = self.processArrival[j]
					self.processArrival[j] = self.processArrival[j+1]
					self.processArrival[j+1] = swap
					# swap process burst times
					swap = self.processBurstTime[j]
					self.processBurstTime[j] = self.processBurstTime[j+1]
					self.processBurstTime[j+1] = swap
					# swap process priorities
					swap = self.processPrioriy[j]
					self.processPrioriy[j] = self.processPrioriy[j+1]
					self.processPrioriy[j+1] = swap
					# swap process name
					swap = self.processName[j]
					self.processName[j] = self.processName[j+1]
					self.processName[j+1] = swap
		print (str(self.processArrival))


	def addBurstTimes(self):
		self.burstTimeTotal = 0
		for i in range(int(self.processCountBox.get())):
			self.burstTimeTotal = self.burstTimeTotal + self.processBurstTime[i]

	def generateProcessesList(self):
		random.seed()
		self.processName = []
		self.processBurstTime = []
		self.processPrioriy = []
		self.processArrival = []
		#remove all elelments in the list
		self.processListBox.delete(0, END)
		for i in range(0, int(self.processCountBox.get())): #maybe check that there is actually a number here
			self.processName.append("P" + str(i+1))
			self.processBurstTime.append(int(random.randint(1,25)))
			self.processPrioriy.append(int(random.randint(1,9)))
			self.processArrival.append(int(i+1))
			processLabel = self.processName[i] + ":  " + str(self.processBurstTime[i]).zfill(2) + "  " + str(self.processPrioriy[i]) + "  " + str(self.processArrival[i]).zfill(2)
			self.processListBox.insert(END, processLabel)

	def checkBurstListForValues(self):
		count = int(self.processCountBox.get())
		for i in range(0, count):
			if self.roundRobinBurstList[i] > 0:
				return False
		return True

	def copyBurstList(self):
		count = int(self.processCountBox.get())
		for i in range(0, count):
			self.roundRobinBurstList.append(self.processBurstTime[i])

	def roundRobinGanttChart(self):
		print("starting round robin...")
		self.setProcessesFrame()
		# get time quanta
		quanta = int(self.timeQuantaBox.get())
		# make copy of burst time list
		self.roundRobinBurstList = []
		self.copyBurstList()
		#print("roundRobinBurstList")
		#print(self.roundRobinBurstList)
		# build the round robin list
		roundRobinBurstQueue = []
		roundRobinNameQueue = []
		quitLoop = self.checkBurstListForValues()
		width = 0
		row = 0
		col = 0
		totalSize = 0
		counter = 0
		processList = []
		while quitLoop == False:
			for i in range(0, int(self.processCountBox.get())):
				print("BurstList[i] before:  "+str(self.roundRobinBurstList[i]))
				if self.roundRobinBurstList[i] > 0:
					leftOver = self.roundRobinBurstList[i] - quanta
					if leftOver <= 0:
						width = self.roundRobinBurstList[i]
					else:
						width = quanta
					#totalSize = totalSize + width

					print("width:  " + str(width))
					roundRobinNameQueue.append(self.processName[i])
					print("Process name:  "+str(roundRobinNameQueue[i]))
					self.roundRobinBurstList[i] = self.roundRobinBurstList[i] - quanta
					print("Burst After:  " + str(self.roundRobinBurstList[i])+"\n")

					# display shapes and calculate size
					Label(self.processDisplay, text=roundRobinNameQueue[i]).grid(row=row, column=col)
					shapeCan = Canvas(self.processDisplay, width=width+1, height=50)
					#processList.append(shapeCan)
					shapeCan.create_rectangle(0, 0, width+1, 50, fill="green")
					shapeCan.grid(row=row+1, column=col)
					# update row and column
					if col > 25:
						col = 0
						row = row + 2
					else:
						col = col + 1

			quitLoop = self.checkBurstListForValues()
			print("----------------------------------------------------------")
		print("name queue")
		print(roundRobinNameQueue)


	def priorityGanttChart(self):
		print("priority...")
		# remove other frame
		self.setProcessesFrame()
		count = int(self.processCountBox.get())
		# sort list by priority
		self.sortProcessesByPriority()
		self.addBurstTimes()
		processList = []
		print("burst: " + str(self.processBurstTime))
		for i in range(0, count):
			Label(self.processDisplay, text=self.processName[i]).grid(row=0, column=i)
			width = (550 / self.burstTimeTotal) * self.processBurstTime[i]
			shapeCan = Canvas(self.processDisplay, width=width, height=50)
			processList.append(shapeCan)
			processList[i].create_rectangle(0, 0, width, 50, fill="yellow")
			processList[i].grid(row=1, column=i, sticky=W)

	def FCFSGanttChart(self):
		print("FCFS...")
		# remove other frame
		self.setProcessesFrame()
		count = int(self.processCountBox.get())
		# sort list by priority
		self.sortProcessesByArrivalTime()
		self.addBurstTimes()
		processList = []
		print("burst: " + str(self.processBurstTime))
		for i in range(0, count):
			Label(self.processDisplay, text=self.processName[i]).grid(row=0, column=i)
			width = (550 / self.burstTimeTotal) * self.processBurstTime[i]
			shapeCan = Canvas(self.processDisplay, width=width, height=50)
			processList.append(shapeCan)
			processList[i].create_rectangle(0, 0, width, 50, fill="red")
			processList[i].grid(row=1, column=i, sticky=W)

	def SJFGanttChart(self):
		print("SJF...")
		# remove old frame
		self.setProcessesFrame()
		count = int(self.processCountBox.get())
		self.sortProcessesByBurstTime()
		self.addBurstTimes()
		processList = []
		print("burst: " + str(self.processBurstTime))
		for i in range(0, count):
			Label(self.processDisplay, text=self.processName[i]).grid(row=0, column=i)
			width = (550 / self.burstTimeTotal) * self.processBurstTime[i]
			shapeCan = Canvas(self.processDisplay, width=width, height=50)
			processList.append(shapeCan)
			processList[i].create_rectangle(0, 0, width, 50, fill="pink")
			processList[i].grid(row=1, column=i, sticky=W)

	def printSelection(self):
		if self.selectedMethod.get() == 0:
			self.roundRobinGanttChart()
		elif self.selectedMethod.get() == 1:
			self.priorityGanttChart()
		elif self.selectedMethod.get() == 2:
			self.SJFGanttChart()
		elif self.selectedMethod.get() == 3:
			self.FCFSGanttChart()

	def setProcessesFrame(self):
		self.processDisplay.grid_remove()
		self.processDisplay = Frame(self.dataColumnFrame, width=600, height=325)
		self.processDisplay.grid_propagate(False);
		self.processDisplay.grid(row=1, column=0)

	def clearProcessFrame(self):
		self.processDisplay.grid_remove()

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

		# set up round robin radio button - command=self.clearProcessFrame,
		self.roundRobinButton = Radiobutton(self.frameRadioButtons, command=self.clearProcessFrame, text="Round Robin", variable=self.selectedMethod, value=0)
		self.roundRobinButton.grid(sticky=N, row=0, column=0)

		# set up shortest job first button
		self.shortestJobFirstButton = Radiobutton(self.frameRadioButtons, command=self.clearProcessFrame, text="Shortest Job First", variable=self.selectedMethod, value=2)
		self.shortestJobFirstButton.grid(sticky=N, row=0, column=1)

		# set up priority button (scheduling)
		self.priorityButton = Radiobutton(self.frameRadioButtons, command=self.clearProcessFrame, text="Priority", variable=self.selectedMethod, value=1)
		self.priorityButton.grid(sticky=N, row=0, column=2)

		# set up button for FCFS
		self.FCFSButton = Radiobutton(self.frameRadioButtons, command=self.clearProcessFrame, text="FCFS", variable=self.selectedMethod, value=3)
		self.FCFSButton.grid(sticky=N, row=0, column=3)

		# default radio button to be selected
		self.roundRobinButton.select()

		# set up frame for where the processes are going to be visually displayed
		self.processDisplay = Frame(self.dataColumnFrame, width=600, height=325)
		self.processDisplay.grid_propagate(False);
		self.processDisplay.grid(row=1, column=0)

		# label and entry for the time quanta - only for round robin
		self.timeQuanta = StringVar()
		Label(self.frameRadioButtons, text="Time Quanta (RR only): ").grid(row=1, column=0)
		self.timeQuantaBox = Entry(self.frameRadioButtons)
		self.timeQuantaBox.grid(row=1, column=1)

		# button for generating the process display
		Button(self.frameRadioButtons, text="Display Gantt Chart", command=self.printSelection).grid(row=1, column=3)

	# def initRoundRobin(self):
	# 	self.roundRobinFrame = Frame(self)
	# 	self.roundRobinFrame.grid(row = 1, column = 2)
	# 	self.timeQuanta = StringVar()
	#
	# 	Label(self.roundRobinFrame, text="Time Quanta: ").grid(row = 0, column =  0)
	# 	self.timeQuantaBox = Entry(self.roundRobinFrame)
	# 	self.timeQuantaBox.grid(row = 0, column = 1)
