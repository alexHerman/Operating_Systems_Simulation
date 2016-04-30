from Tkinter import *
from processFrame import *
from memoryFrame import *

def processWindow():
	processframe = processFrame()
def memoryWindow():
	memoryframe = memoryFrame()
def pageFrame():
	print("Test")

def main():
	root = Tk()

	processButton = Button(root, text="Process Scheduler Algorithms", command=processWindow)
	memoryButton = Button(root, text="Memory Management Algorithms", command=memoryWindow)
	pageButton = Button(root, text="Page Replacement Algorithms", command=pageFrame)

	processButton.pack()
	memoryButton.pack()
	pageButton.pack()

	root.mainloop()

if __name__ == '__main__':
    main()
