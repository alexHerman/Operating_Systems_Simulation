'''
Description: This class handles all of the page replacement algorithms. It builds
a new frame and shows text boxes for the options that can be chosen by the user.
It generates a reference string based on the user's selection and displays the
page table after each page fault that occurs.
'''

from Tkinter import *
import random

class pageFrame(Frame):
	def __init__(self):
		self.parent = Tk()
		self.parent.geometry("900x700+100+100")
		Frame.__init__(self, self.parent)
		self.grid()
		self.initUI()
		self.memory = []
		self.accessed = []
		self.memorySize = 3
		self.parent.mainloop()

	def initUI(self):
		self.parent.title("Page Replacement Algorithms")

		Label(self, text="Number of Frames: ").grid(row = 1, column =  0)
		self.numberOfFrames = Entry(self)
		self.numberOfFrames.grid(row = 1, column = 1)
		Label(self, text="Size of Reference String: ").grid(row = 1, column =  2)
		self.sizeOfReferenceString = Entry(self)
		self.sizeOfReferenceString.grid(row = 1, column = 3)

		self.updateButton = Button(self, text="Update", command=self.update)
		self.updateButton.grid(row = 1, column=5)

		self.selectedMethod = IntVar(master=self.parent)
		self.frameRadioButtons = Frame(self)
		self.frameRadioButtons.grid(row=0, column=0, columnspan=30, sticky=W)

		#Set up the algorithm radio buttons
		self.FIFO = Radiobutton(self.frameRadioButtons, command=self.update, text="FIFO", variable=self.selectedMethod, value=0)
		self.FIFO.grid(row=0, column=0)

		self.Optimal = Radiobutton(self.frameRadioButtons, command=self.update, text="Optimal", variable=self.selectedMethod, value=1)
		self.Optimal.grid(row=0, column=1)

		self.LRU = Radiobutton(self.frameRadioButtons, command=self.update, text="LRU", variable=self.selectedMethod, value=2)
		self.LRU.grid(row=0, column=2)

		self.LFU = Radiobutton(self.frameRadioButtons, command=self.update, text="LFU", variable=self.selectedMethod, value=3)
		self.LFU.grid(row=0, column=3)

		self.NRU = Radiobutton(self.frameRadioButtons, command=self.update, text="NRU", variable=self.selectedMethod, value=4)
		self.NRU.grid(row=0, column=4)


		self.insertFrame = Frame(self)
		self.insertFrame.grid(row = 2, column = 0, columnspan=30, rowspan=30, sticky=S)
		self.grid_rowconfigure(2, minsize=100)

	#Runs the theoretically optimal algorithm of page replacement
	def optimal(self):
		refString = []
		self.memory = []
		self.accessed = []
		self.insertFrame.grid_remove()
		self.insertFrame = Frame(self)
		self.insertFrame.grid(row = 2, column = 0, columnspan=30, rowspan=30, sticky=S)
		for i in range(0, int(self.sizeOfReferenceString.get())):
			refString.insert(0, random.randrange(0, int(self.numberOfFrames.get())))

		for i in range(0, len(refString)):
			page = refString[i]
			Label(self.insertFrame, text=str(page)).grid(row=2 * (i//20), column=i % 20)
			b = Listbox(self.insertFrame, height = self.memorySize, width = 2)
			self.insertFrame.grid_columnconfigure(i, minsize=40)
			#Finds the page reference furthest from the current location
			if page not in self.memory:
				if len(self.memory) == self.memorySize:
					farthestDist = 0
					farthestIndex = 0
					for j in range(0, len(self.memory)):
						for k in range(i + 1, len(refString)):
							if k == len(refString) - 1:
									farthestDist = k
									farthestIndex = j
							if self.memory[j] == refString[k]:
								if k > farthestDist:
									farthestDist = k
									farthestIndex = j
								break
					self.memory.remove(self.memory[farthestIndex])
					self.memory.insert(farthestIndex, page)
				else:
					self.memory.insert(0, page)
				for j in range(0, len(self.memory)):
					b.insert(END, self.memory[j])
				b.grid(row=2 * (i//20) + 1, column=i%20)

	#Runs a simulation of the not recently used algorithm
	def NRUalgorithm(self):
		refString = []
		self.memory = []
		self.referenced = []
		self.modified = []
		self.insertFrame.grid_remove()
		self.insertFrame = Frame(self)
		self.insertFrame.grid(row = 2, column = 0, columnspan=30, rowspan=30, sticky=S)
		for i in range(0, int(self.sizeOfReferenceString.get())):
			refString.insert(0, random.randrange(0, int(self.numberOfFrames.get())))

		for i in range(0, len(refString)):
			page = refString[i]
			if i % 5 == 0:
				self.resetReferenced()
			Label(self.insertFrame, text=str(page)).grid(row=2 * (i//20), column=i % 20)
			b = Listbox(self.insertFrame, height = self.memorySize, width = 2)
			self.insertFrame.grid_columnconfigure(i, minsize=40)
			found = False
			index = 0
			if page not in self.memory:
				if len(self.memory) == self.memorySize:
					#Find if there exists a page in memory that fits into any of the four categories
					#Prioritizes pages in the lowest category
					for j in range(0, len(self.memory)):
						if self.modified[j] == 0 and self.referenced[j] == 0:
							found = True
							index = j
					if found == False:
						for j in range(0, len(self.memory)):
							if self.modified[j] == 1 and self.referenced[j] == 0:
								found = True
								index = j
					if found == False:
						for j in range(0, len(self.memory)):
							if self.modified[j] == 0 and self.referenced[j] == 1:
								found = True
								index = j
					if found == False:
						for j in range(0, len(self.memory)):
							if self.modified[j] == 1 and self.referenced[j] == 1:
								found = True
								index = j
					self.memory[index] = page
					self.referenced[index] = 1
					self.modified[index] = 0
				else:
					self.memory.insert(0, page)
					self.referenced.insert(0, 1)
					self.modified.insert(0, 0)
				for j in range(0, len(self.memory)):
					b.insert(END, self.memory[j])
				b.grid(row=2 * (i//20) + 1, column=i%20)
			else:
				if self.modified[self.memory.index(page)] == 0:
						self.modified[self.memory.index(page)] = random.randrange(0, 1)

	#Resets the "referenced" bit on each page
	def resetReferenced(self):
		for i in range(0, len(self.referenced)):
			self.referenced[i] = 0

	#Called upon clicking update or choosing a new radio button, runs the correct algorithm
	def update(self):
		if self.selectedMethod.get() == 1:
			self.optimal()
		elif self.selectedMethod.get() == 4:
			self.NRUalgorithm()
		else:
			self.fault = False
			self.memory = []
			self.accessed = []
			self.insertFrame.grid_remove()
			self.insertFrame = Frame(self)
			self.insertFrame.grid(row = 2, column = 0, columnspan=30, rowspan=30, sticky=S)
			for i in range(0, int(self.sizeOfReferenceString.get())):
				ref = random.randrange(0, int(self.numberOfFrames.get()))
				Label(self.insertFrame, text=str(ref)).grid(row=2 * (i//20), column=i % 20)

				b = Listbox(self.insertFrame, height = self.memorySize, width = 2)
				self.insertFrame.grid_columnconfigure(i, minsize=40)
				self.loadPage(ref, b, i)
				
				if self.fault == True:
					b.grid(row=2 * (i//20) + 1, column=i%20)
				self.fault = False

	#Based on the algorithm selected, this method does the actual page replacement
	def loadPage(self, page, lBox, time):
		if page not in self.memory:
			self.fault = True
			# FIFO
			if self.selectedMethod.get() == 0:
				if len(self.memory) == self.memorySize:
					self.memory.remove(self.memory[len(self.memory) - 1])
				self.memory.insert(0, page)

			# LRU
			if self.selectedMethod.get() == 2:
				LRUIndex = 0
				if len(self.memory) == self.memorySize:
					for i in range(0, len(self.memory)):
						if self.accessed[i] < self.accessed[LRUIndex]:
							LRUIndex = i
					self.memory.remove(self.memory[LRUIndex])
					self.accessed.remove(self.accessed[LRUIndex])
				self.memory.insert(LRUIndex, page)
				self.accessed.insert(LRUIndex, time)

			# LFU
			if self.selectedMethod.get() == 3:
				LFUIndex = 0
				if len(self.memory) == self.memorySize:
					for i in range(0, len(self.memory)):
						if self.accessed[i] < self.accessed[LFUIndex]:
							LFUIndex = i
					self.memory.remove(self.memory[LFUIndex])
					self.accessed.remove(self.accessed[LFUIndex])
				self.memory.insert(LFUIndex, page)
				self.accessed.insert(LFUIndex, 1)

		else:
			if self.selectedMethod.get() == 2:
				self.accessed[self.memory.index(page)] = time
			if self.selectedMethod.get() == 3:
				self.accessed[self.memory.index(page)] += 1
		for i in range(0, len(self.memory)):
			lBox.insert(END, self.memory[i])
