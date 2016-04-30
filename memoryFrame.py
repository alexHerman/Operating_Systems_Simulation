from Tkinter import *
import random
import time

waitTime = 500

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
		Label(self, text="Number of Frames: ").grid(row = 0, column =  0)
		self.numberOfFrames = Entry(self)
		self.numberOfFrames.grid(row = 0, column = 2)
		Label(self, text="Number of Pages: ").grid(row = 0, column =  3)
		self.numberOfPages = Entry(self)
		self.numberOfPages.grid(row = 0, column = 4)
		self.startButton = Button(self, text="Start", command=self.initMMU)
		self.startButton.grid(row = 0, column=5)

	def initMMU(self):
		self.startButton.grid_remove()
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
		TLBTableNumbers = Listbox(self, width=3, height = 5)
		for i in range(0, 5):
			TLBTableNumbers.insert(END, i)
		TLBTableNumbers.grid(row = 4, column=1)
		TLBTableNumbers.config(bg = "gray93", border = 0)
		Label(self, text="Page").grid(row = 3, column = 2)
		self.TLBpages = Listbox(self)
		self.TLBpages.grid(row = 4, column = 2)
		self.TLBpages.config(height=5)
		Label(self, text="Frame").grid(row = 3, column = 3)
		self.TLBframes = Listbox(self)
		self.TLBframes.grid(row = 4, column = 3)
		self.TLBframes.config(height=5)
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

	def fillPageTable(self):
		for i in range(0, int(self.numberOfPages.get())):
			frame = random.randrange(0, int(self.numberOfFrames.get()))
			while frame in self.pageTable.get(0, END):
				frame = random.randrange(0, int(self.numberOfFrames.get()))
			self.pageTable.insert(0, frame)

	def fillFrameTable(self):
		for i in range(0, int(self.numberOfFrames.get())):
			self.RAM.insert(END, "Frame " + str(i))

	def animate(self):
		self.resetTables()
		self.page = random.randrange(0, int(self.numberOfPages.get()))
		self.offset = random.randrange(0, 32)
		self.addressPage.delete(0, END)
		self.addressPage.insert(0, str(self.page))
		self.addressOffset.delete(0, END)
		self.addressOffset.insert(0, str(self.offset))
		self.parent.after(waitTime, self.updateTLB)

	def updateTLB(self):
		inTLB = False
		for i in range(0, 5):
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

	def updatePageTable(self):
		self.pageTable.itemconfig(self.page, bg="green")
		self.frame = self.pageTable.get(self.page)
		if self.TLBpages.size() == 5:
			self.TLBpages.delete(END)
			self.TLBframes.delete(END)
		self.TLBpages.insert(0, self.page)
		self.TLBframes.insert(0, self.pageTable.get(self.page))
		self.parent.after(waitTime, self.updatePhysicalAddress)

	def updatePhysicalAddress(self):
		self.physicalAddressPage.delete(0, END)
		self.physicalAddressPage.insert(0, str(self.frame))
		self.physicalAddressOffset.delete(0, END)
		self.physicalAddressOffset.insert(0, str(self.addressOffset.get()))
		self.parent.after(waitTime, self.updateRAM)

	def updateRAM(self):
		self.RAM.itemconfig(self.frame, bg="green")
		self.parent.after(waitTime, self.animate)

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
