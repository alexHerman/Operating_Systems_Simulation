from Tkinter import *
from processFrame import *
from memoryFrame import *
from pageFrame import *

def processWindow():
	processframe = processFrame()
def memoryWindow():
	memoryframe = memoryFrame()
def pageWindow():
	pageframe = pageFrame()

def main():
	root = Tk()
	root.title("Program 4 - CSC456")

	processButton = Button(root, text="Process Scheduler Algorithms", command=processWindow)
	memoryButton = Button(root, text="Memory Management Algorithms", command=memoryWindow)
	pageButton = Button(root, text="Page Replacement Algorithms", command=pageWindow)

	processButton.pack()
	memoryButton.pack()
	pageButton.pack()

	root.mainloop()

if __name__ == '__main__':
    main()
