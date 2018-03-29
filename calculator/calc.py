from Tkinter import *

class Application(Frame):
    #GLOBAL VARIABLES
    global calcView
    calcView = "0"

    #METHODS
    def clear(self):
        self.view.config(text="0")

    def changeSign(self):
    	print "CHANGE SIGN PLUS -> MINUS AND VICE VERSA"

    def takePercent(self):
        print "TAKE PERCENT"

    def doDivision(self):
        print "/"

    def doMultiplication(self):
        print "X"

    def doSubtraction(self):
        print "-"

    def doAddition(self):
        print "+"

    def doEquals(self):
        print "="

    def printOne(self):
        if "0" not in self.view.cget("text"):
            self.view.config(text="1")
        else:
            

    def printTwo(self):
        print "2"

    def printThree(self):
        print "3"

    def printFour(self):
        print "4"

    def printFive(self):
        print "5"

    def printSix(self):
        print "6"

    def printSeven(self):
        print "7"

    def printEight(self):
        print "8"

    def printNine(self):
        print "9"

    def printZero(self):
        print "0"

    def printDot(self):
        print "."

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

        self.multiply = Button(self)
        self.multiply["text"] = "X"
        self.multiply["command"] =  self.doMultiplication

        self.minus = Button(self)
        self.minus["text"] = "-"
        self.minus["command"] =  self.doSubtraction

        self.add = Button(self)
        self.add["text"] = "+"
        self.add["command"] =  self.doAddition

        self.equals = Button(self)
        self.equals["text"] = "="
        self.equals["command"] =  self.doEquals

        self.one = Button(self)
        self.one["text"] = "1"
        self.one["command"] =  self.printOne

        self.two = Button(self)
        self.two["text"] = "2"
        self.two["command"] =  self.printTwo

        self.three = Button(self)
        self.three["text"] = "3"
        self.three["command"] =  self.printThree

        self.four = Button(self)
        self.four["text"] = "4"
        self.four["command"] =  self.printFour

        self.five = Button(self)
        self.five["text"] = "5"
        self.five["command"] =  self.printFive

        self.six = Button(self)
        self.six["text"] = "6"
        self.six["command"] =  self.printSix

        self.seven = Button(self)
        self.seven["text"] = "7"
        self.seven["command"] =  self.printSeven

        self.eight = Button(self)
        self.eight["text"] = "8"
        self.eight["command"] =  self.printEight

        self.nine = Button(self)
        self.nine["text"] = "9"
        self.nine["command"] =  self.printNine

        self.zero = Button(self)
        self.zero["text"] = "0"
        self.zero["command"] =  self.printZero

        self.dot = Button(self)
        self.dot["text"] = "."
        self.dot["command"] =  self.printDot

        #GRID ALL THE BUTTONS TOGETHER
        self.view = Label(self, text=calcView, anchor="e")
        self.view.grid(row=1,columnspan=100)

        self.allClear.grid(row=2,column=1)
        self.plusMinus.grid(row=2,column=2)
        self.percent.grid(row=2,column=3)
        self.divide.grid(row=2,column=4)

        self.seven.grid(row=3,column=1)
        self.eight.grid(row=3,column=2)
        self.nine.grid(row=3,column=3)
        self.multiply.grid(row=3,column=4)

        self.four.grid(row=4,column=1)
        self.five.grid(row=4,column=2)
        self.six.grid(row=4,column=3)
        self.minus.grid(row=4,column=4)

        self.one.grid(row=5,column=1)
        self.two.grid(row=5,column=2)
        self.three.grid(row=5,column=3)
        self.add.grid(row=5,column=4)

        self.zero.grid(row=6,columnspan=2)
        self.dot.grid(row=6,column=3)
        self.equals.grid(row=6,column=4)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()