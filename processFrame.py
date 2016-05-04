from Tkinter import *
import random

###########################################################################
# Author: Alex Herman, Andrew Fagrey
# Description: Class that contains the code for the process scheduler part
#  of the 4th CSC456 program.
###########################################################################
class processFrame(Frame):

	###########################################################################
	# Author: Alex Herman, Andrew Fagrey
	# Description: This function is the class constructor
	###########################################################################
	def __init__(self):
		self.parent = Tk()
		self.parent.title("Process Management Algorithms")
		self.parent.geometry("800x400+300+300")
		Frame.__init__(self, self.parent)
		self.grid()

		self.initUI();
		self.parent.mainloop()
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: This function is responsible for sorting the process lists
	#  by their priority
	###########################################################################
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
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: This function is responsible for sorting the process lists
	#  by their burst times
	###########################################################################
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
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: This function is responsible for sorting the process lists
	#  by their arrival time
	###########################################################################
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
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: This function adds the process burst times and stores the
	#  total in a global variable
	###########################################################################
	def addBurstTimes(self):
		self.burstTimeTotal = 0
		for i in range(int(self.processCountBox.get())):
			self.burstTimeTotal = self.burstTimeTotal + self.processBurstTime[i]
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: This function generates the process list
	###########################################################################
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
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: This function checks that a copy of the burst list still has
	#  values that are greater than zero in it
	###########################################################################
	def checkBurstListForValues(self):
		count = int(self.processCountBox.get())
		for i in range(0, count):
			if self.roundRobinBurstList[i] > 0:
				return False
		return True
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: A function to copy the processBurstTime list to another list
	###########################################################################
	def copyBurstList(self):
		count = int(self.processCountBox.get())
		for i in range(0, count):
			self.roundRobinBurstList.append(self.processBurstTime[i])
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: Function for generating the gantt chart for Priority Sch.
	###########################################################################
	def roundRobinGanttChart(self):
		# clear the frames
		self.setProcessesFrame()

		# get time quanta
		quanta = int(self.timeQuantaBox.get())

		# make copy of burst time list
		self.roundRobinBurstList = []
		self.copyBurstList()

		# build the round robin list
		roundRobinBurstQueue = []
		roundRobinNameQueue = []

		# set up initial loop condition variable
		quitLoop = self.checkBurstListForValues()

		# variables used in the loop below
		width = 0
		row = 0
		col = 0
		totalTime = 0
		processList = []
		colT = 0

		# keep looping through the burst list till all values are less then zero
		while quitLoop == False:
			for i in range(0, int(self.processCountBox.get())):
				if self.roundRobinBurstList[i] > 0:
					leftOver = self.roundRobinBurstList[i] - quanta
					if leftOver <= 0:
						width = self.roundRobinBurstList[i]
					else:
						width = quanta
					roundRobinNameQueue.append(self.processName[i])
					self.roundRobinBurstList[i] = self.roundRobinBurstList[i] - quanta
					# display shapes and calculate size
					Label(self.processDisplay, text=roundRobinNameQueue[i]).grid(row=row, column=col)
					shapeCan = Canvas(self.processDisplay, width=width+1, height=50)
					shapeCan.create_rectangle(0, 0, width+1, 50, fill="green")
					shapeCan.grid(row=row+1, column=col)
					# update row and column
					if col > 25:
						col = 0
						row = row + 2
					else:
						col = col + 1

					# display the label for burst time
					#Label(self.processDisplay, text=str(totalTime)).grid(row=row+2, column=col)

			quitLoop = self.checkBurstListForValues()
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: Function for generating the gantt chart for Priority Sch.
	###########################################################################
	def priorityGanttChart(self):
		# clear the window of other gantt charts
		self.setProcessesFrame()

		# sort list by priority
		self.sortProcessesByPriority()

		# add the burst times (used for calculating the width of the shapes)
		self.addBurstTimes()

		# some variables used below in the loop
		processList = []
		col = 0
		totalTime = 0

		# loop through the number of processes and display the gantt chart
		for i in range(0, int(self.processCountBox.get())):
			# show the process label
			Label(self.processDisplay, text=self.processName[i]).grid(row=0, column=col+1)

			# calculate the width of the shape
			width = (300 / self.burstTimeTotal) * self.processBurstTime[i]

			# add to the shape the process list and display it in the window
			shapeCan = Canvas(self.processDisplay, width=width, height=50)
			processList.append(shapeCan)
			processList[i].create_rectangle(0, 0, width, 50, fill="yellow")
			processList[i].grid(row=1, column=col+1, sticky=W)

			# display the label for burst time
			Label(self.processDisplay, text=str(totalTime)).grid(row=2, column=col)

			# get the total time so far and increase column value
			totalTime = totalTime + self.processBurstTime[i]
			col = col + 2
		# End of for loop

		# add remaining burst time label to window
		Label(self.processDisplay, text=str(totalTime)).grid(row=2, column=col)
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: Function for generating the gantt chart for FCFS
	###########################################################################
	def FCFSGanttChart(self):
		# clear the window of other gantt charts
		self.setProcessesFrame()

		# sort list by arrival time
		self.sortProcessesByArrivalTime()

		# add the burst times (used for calculating the width of the shapes)
		self.addBurstTimes()

		# some variables used below in the loop
		processList = []
		col = 0
		totalTime = 0

		# loop through the number of processes and display the gantt chart
		for i in range(0, int(self.processCountBox.get())):
			# show the process label
			Label(self.processDisplay, text=self.processName[i]).grid(row=0, column=col+1)

			# calculate the width of the shape
			width = (300 / self.burstTimeTotal) * self.processBurstTime[i]

			# add to the shape the process list and display it in the window
			shapeCan = Canvas(self.processDisplay, width=width, height=50)
			processList.append(shapeCan)
			processList[i].create_rectangle(0, 0, width, 50, fill="red")
			processList[i].grid(row=1, column=col+1, sticky=W)

			# display the label for burst time
			Label(self.processDisplay, text=str(totalTime)).grid(row=2, column=col)

			# get the total time so far and increase column value
			totalTime = totalTime + self.processBurstTime[i]
			col = col + 2
		# End of for loop

		# add remaining burst time label to window
		Label(self.processDisplay, text=str(totalTime)).grid(row=2, column=col)
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: Function for generating the gantt chart for SJF
	###########################################################################
	def SJFGanttChart(self):
		# clear the window of other gantt charts
		self.setProcessesFrame()

		# sort the processes by burst time and calculate total burst time
		self.sortProcessesByBurstTime()
		self.addBurstTimes()

		# vars used in loop below
		processList = []
		col = 0
		totalTime = 0

		# loop through the processes and display the gantt chart
		for i in range(0, int(self.processCountBox.get())):
			# show the process label
			Label(self.processDisplay, text=self.processName[i]).grid(row=0, column=col+1)

			# calculate the width of the shape
			width = (300 / self.burstTimeTotal) * self.processBurstTime[i]

			# add to the shape the process list and display it in the window
			shapeCan = Canvas(self.processDisplay, width=width, height=50)
			processList.append(shapeCan)
			processList[i].create_rectangle(0, 0, width, 50, fill="blue")
			processList[i].grid(row=1, column=col+1, sticky=W)

			# display the label for burst time
			Label(self.processDisplay, text=str(totalTime)).grid(row=2, column=col)

			# get the total time so far and increase column value
			totalTime = totalTime + self.processBurstTime[i]
			col = col + 2
		# End of for loop

		# add remaining burst time label to window
		Label(self.processDisplay, text=str(totalTime)).grid(row=2, column=col)
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: A function to select (based on the radio button selected)
	#  which process scheduling algorithm to run
	###########################################################################
	def printSelection(self):
		if self.selectedMethod.get() == 0:
			self.roundRobinGanttChart()
		elif self.selectedMethod.get() == 1:
			self.priorityGanttChart()
		elif self.selectedMethod.get() == 2:
			self.SJFGanttChart()
		elif self.selectedMethod.get() == 3:
			self.FCFSGanttChart()
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: A function to set the processes display frame
	###########################################################################
	def setProcessesFrame(self):
		self.processDisplay.grid_remove()
		self.processDisplay = Frame(self.dataColumnFrame, width=600, height=325)
		self.processDisplay.grid_propagate(False);
		self.processDisplay.grid(row=1, column=0)
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: A function for removing the process display frame
	###########################################################################
	def clearProcessFrame(self):
		self.processDisplay.grid_remove()
	############################# END OF FUNCTION #############################

	###########################################################################
	# Author: Andrew Fagrey
	# Description: This function is responsible for laying out the frames for
	#  the various elements of the process scheduling UI
	###########################################################################
	def initUI(self):
		# FRAME FOR PROCESS LIST ON THE LEFT SIDE OF THE WINDOW
		# set up left side column for processes
		self.processListColumnFrame = Frame(self, width=200, height=400, background="grey")
		self.processListColumnFrame.grid_propagate(False);
		self.processListColumnFrame.grid(row=0, column=0)

		# process list
		# show label and entry box for process count
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
	############################# END OF FUNCTION #############################
