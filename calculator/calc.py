from Tkinter import *

class Application(Frame):
    def clear(self):
        print "ALL CLEAR"

    def changeSign(self):
    	print "CHANGE SIGN PLUS -> MINUS AND VICE VERSA"

    def takePercent(self):
        print "TAKE PERCENT"

    def doDivision(self):
        print "DO DIVISION"

    def doMultiplication(self):
        print "DO MULTIPLICATION"

    def doSubtraction(self):
        print "DO SUBTRACTION"

    def doAddition(self):
        print "DO ADDITION"

    def doEquals(self):
        print "DO EQUALS"

    def printSeven(self):
        print "7"

    def printEight(self):
        print "8"

    def printNine(self):
        print "9"

    def createWidgets(self):
        #FIRST ROW OF BUTTONS 
        #AC(ALL CLEAR) BUTTON
        self.allClear = Button(self)
        self.allClear["text"] = "AC"
        self.allClear["fg"]   = "red"
        self.allClear["command"] =  self.clear

        #PLUS MINUS BUTTON
        self.plusMinus = Button(self)
        self.plusMinus["text"] = "+/-"
        self.plusMinus["command"] = self.changeSign

        #TAKE PERCENTAGE BUTTON
        self.percent = Button(self)
        self.percent['text'] = "%"
        self.percent['command'] = self.takePercent

        #DIVISION BUTTON
        self.divide = Button(self)
        self.divide["text"] = "/"
        self.divide["fg"]   = "red"
        self.divide["command"] =  self.doDivision

        self.seven = Button(self)
        self.seven["text"] = "7"
        self.seven["command"] =  self.printSeven

        self.eight = Button(self)
        self.eight["text"] = "8"
        self.eight["command"] =  self.printEight

        self.nine = Button(self)
        self.nine["text"] = "9"
        self.nine["command"] =  self.printNine

        self.multiply = Button(self)
        self.nine["text"] = "X"
        self.nine["command"] =  self.doMultiplication

        #GRID ALL THE BUTTONS TOGETHER
        self.allClear.grid(row=1,column=1)
        self.plusMinus.grid(row=1,column=2)
        self.percent.grid(row=1,column=3)
        self.divide.grid(row=1,column=4)

        self.seven.grid(row=2,column=1)
        self.eight.grid(row=2,column=2)
        self.nine.grid(row=2,column=3)
        self.multiply.grid(row=2,column=4)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()