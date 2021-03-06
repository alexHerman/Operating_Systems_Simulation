from Tkinter import *
import random

waitTime = 5000

class memoryFrame(Frame):
	def __init__(self):
		self.parent = Tk()
		self.parent.title("Memory Management")
		self.parent.geometry("900x700+100+100")
		Frame.__init__(self, self.parent)
		self.grid()
		self.total = 0
		self.TLBhits = 0
		self.alpha = 0.0

		self.initUI();
		self.parent.mainloop()

	def printSelection(self):
		print(self.timeQuantaBox.get())

	def initUI(self):
		self.inputFrame = Frame(self)
		self.inputFrame.grid(row=0, column=0, columnspan=100, sticky=W)

		#Number of frames text box
		Label(self.inputFrame, text="Number of Frames: ").grid(row = 0, column =  0)
		self.numberOfFrames = Entry(self.inputFrame)
		self.numberOfFrames.grid(row = 0, column = 1)

		#Number of pages text box
		Label(self.inputFrame, text="Number of Pages: ").grid(row = 0, column =  2)
		self.numberOfPages = Entry(self.inputFrame)
		self.numberOfPages.grid(row = 0, column = 3)

		#TLB size text box
		Label(self.inputFrame, text="TLB Size: ").grid(row = 0, column =  4)
		self.TLBSize = Entry(self.inputFrame)
		self.TLBSize.grid(row = 0, column = 5)

		#Start button
		self.startButton = Button(self.inputFrame, text="Start", command=self.initMMU)
		self.startButton.grid(row = 0, column=6)

	#Initializes the memory management GUI componenets
	def initMMU(self):
		self.startButton.grid_remove()
		#Create a text box for the logical address
		Label(self, text="Logical Address: ").grid(row = 1, column = 0, sticky=S)
		self.addressPage = Entry(self)
		self.addressPage.grid(row = 1, column = 2, sticky=S)
		self.addressOffset = Entry(self)
		self.addressOffset.grid(row = 1, column = 3, sticky=S)
		self.grid_rowconfigure(1, minsize=40)
		Label(self, text="Physical Address: ").grid(row = 1, column = 4, sticky=S)
		self.physicalAddressPage = Entry(self)
		self.physicalAddressPage.grid(row = 1, column = 5, sticky=S)
		self.physicalAddressOffset = Entry(self)
		self.physicalAddressOffset.grid(row = 1, column = 6, sticky=S, columnspan=2)

		# TLB
		Label(self, text="TLB:").grid(row = 4, column = 0)
		TLBTableNumbers = Listbox(self, width=3, height = int(self.TLBSize.get()))
		for i in range(0, int(self.TLBSize.get())):
			TLBTableNumbers.insert(END, i)
		TLBTableNumbers.grid(row = 4, column=1)
		TLBTableNumbers.config(bg = "gray93", border = 0)
		Label(self, text="Page").grid(row = 3, column = 2)
		self.TLBpages = Listbox(self)
		self.TLBpages.grid(row = 4, column = 2)
		self.TLBpages.config(height=int(self.TLBSize.get()))
		Label(self, text="Frame").grid(row = 3, column = 3)
		self.TLBframes = Listbox(self)
		self.TLBframes.grid(row = 4, column = 3)
		self.TLBframes.config(height=int(self.TLBSize.get()))
		self.grid_rowconfigure(2, minsize=50)

		# Page Table
		Label(self, text="Page Table:").grid(row = 5, column = 0)
		pageTableNumbers = Listbox(self, width=3, height = int(self.numberOfPages.get()))
		for i in range(0, int(self.numberOfPages.get())):
			pageTableNumbers.insert(END, i)
		pageTableNumbers.grid(row = 5, column=1)
		pageTableNumbers.config(bg = "gray93", border = 0)
		self.pageTable = Listbox(self)
		self.pageTable.grid(row = 5, column = 2)
		self.pageTable.config(height=self.numberOfPages.get())
		self.grid_rowconfigure(5, minsize=300)
		self.fillPageTable()
		Label(self, text="Effective Access Time: ").grid(row=6, column = 0)
		self.EAT = Entry(self)
		self.EAT.grid(row = 6, column = 2)
		self.grid_rowconfigure(6, minsize=40)

		#RAM table
		Label(self, text="Physical Memory:").grid(row=3, column=5, rowspan=10)
		frameTableNumbers = Listbox(self, width=3, height = int(self.numberOfFrames.get()))
		for i in range(0, int(self.numberOfFrames.get())):
			frameTableNumbers.insert(END, i)
		frameTableNumbers.grid(row = 3, column=6, rowspan=10)
		frameTableNumbers.config(bg = "gray93", border = 0)
		self.RAM = Listbox(self)
		self.RAM.grid(row = 3, column = 7, rowspan=10)
		self.RAM.config(height=int(self.numberOfFrames.get()))
		self.grid_columnconfigure(6, minsize=100)
		self.fillFrameTable()
		self.animate();

	#Randomly generates the page table
	def fillPageTable(self):
		for i in range(0, int(self.numberOfPages.get())):
			frame = random.randrange(0, int(self.numberOfFrames.get()))
			while frame in self.pageTable.get(0, END):
				frame = random.randrange(0, int(self.numberOfFrames.get()))
			self.pageTable.insert(0, frame)

	#Assigns labels to each frame in RAM
	def fillFrameTable(self):
		for i in range(0, int(self.numberOfFrames.get())):
			self.RAM.insert(END, "Frame " + str(i))

	#Begins animating the diagram. Starts by creating a logical address
	def animate(self):
		self.resetTables()
		self.page = random.randrange(0, int(self.numberOfPages.get()))
		self.offset = random.randrange(0, 32)
		self.addressPage.delete(0, END)
		self.addressPage.insert(0, str(self.page))
		self.addressOffset.delete(0, END)
		self.addressOffset.insert(0, str(self.offset))
		self.parent.after(waitTime, self.updateTLB)

	#Checks if the page is in the TLB and if it is not, goes to the page table
	def updateTLB(self):
		inTLB = False
		for i in range(0, int(self.TLBSize.get())):
			if self.TLBpages.get(i) == self.page:
				self.TLBpages.itemconfig(i, bg = "green")
				self.TLBhits = self.TLBhits + 1
				self.total = self.total + 1
				self.alpha = float(self.TLBhits) / self.total
				inTLB = True
				self.TLBpages.activate(i)
				self.TLBframes.activate(i)
				self.frame = self.TLBframes.get(i)
				self.parent.after(waitTime, self.updatePhysicalAddress)

		if inTLB == False:
			self.total = self.total + 1
			self.alpha = float(self.TLBhits) / self.total
			self.TLBpages.config(bg = "red")
			for i in range(0, self.TLBpages.size()):
				self.TLBpages.itemconfig(i, bg="red")
			self.parent.after(waitTime, self.updatePageTable)

		self.EAT.delete(0, END)
		self.EAT.insert(0, str(round(self.alpha * 100 + (1 - self.alpha) * 200, 3)))

	#Called if a page was not in the TLB, finds the page in the page table and updates the TLB
	def updatePageTable(self):
		self.pageTable.itemconfig(self.page, bg="green")
		self.frame = self.pageTable.get(self.page)
		if self.TLBpages.size() == int(self.TLBSize.get()):
			self.TLBpages.delete(END)
			self.TLBframes.delete(END)
		self.TLBpages.insert(0, self.page)
		self.TLBframes.insert(0, self.pageTable.get(self.page))
		self.parent.after(waitTime, self.updatePhysicalAddress)

	#Updates the text boxes that display the physical address
	def updatePhysicalAddress(self):
		self.physicalAddressPage.delete(0, END)
		self.physicalAddressPage.insert(0, str(self.frame))
		self.physicalAddressOffset.delete(0, END)
		self.physicalAddressOffset.insert(0, str(self.addressOffset.get()))
		self.parent.after(waitTime, self.updateRAM)

	#Highlights the correct frame in RAM
	def updateRAM(self):
		self.RAM.itemconfig(self.frame, bg="green")
		self.parent.after(waitTime, self.animate)

	#Resets the colors on each of the tables
	def resetTables(self):
		for i in range(0, int(self.numberOfPages.get())):
			self.pageTable.itemconfig(i, bg="white")

		for i in range(0, int(self.numberOfFrames.get())):
			self.RAM.itemconfig(i, bg="white")

		for i in range(0, self.TLBpages.size()):
			self.TLBpages.itemconfig(i, bg="white")
		self.TLBpages.config(bg = "white")
		self.physicalAddressPage.delete(0, END)
		self.physicalAddressOffset.delete(0, END)
