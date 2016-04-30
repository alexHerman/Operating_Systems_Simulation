from Tkinter import *
from processFrame import *

def processWindow():
	processframe = processFrame()
def memoryFrame():
	print("Test")
def pageFrame():
	print("Test")

def main():
	root = Tk()
	root.title("Program 4 - CSC456")

	processButton = Button(root, text="Process Scheduler Algorithms", command=processWindow)
	memoryButton = Button(root, text="Memory Management Algorithms", command=memoryFrame)
	pageButton = Button(root, text="Page Replacement Algorithms", command=pageFrame)

	processButton.pack()
	memoryButton.pack()
	pageButton.pack()

	root.mainloop()

if __name__ == '__main__':
    main()
