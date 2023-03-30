from tkinter import *
class MyWindow:
    def __init__(self, win):

#widgets start from here
        self.lbl1 = Label(win, text="1st No.")
        self.lbl1.place(x=100, y=50)
        self.lbl2 = Label(win, text= "2nd No.")
        self.lbl2.place(x=100, y=100)
        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=100, y=150)
        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=200, y=50)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=200, y=100)
        self.txt3 = Entry(win, bd=3)
        self.txt3.place(x=200, y=150)
        self.btnadd = Button(win, text="Add")
        self.btnadd.place(x=100, y=200)
        self.btnadd.bind('<Button-1>', self.add)
        self.btnsub = Button(win,text="Subtract")
        self.btnsub.place(x=150,y=200)
        self.btnsub.bind('<Button-1>',self.sub)
        self.btnml = Button(win, text="Multiply", command = self.ml)
        self.btnml.place(x = 225, y = 200)
        self.btndiv = Button(win, text="Divide", command = self.div)
        self.btndiv.place(x = 300, y = 200)
        self.btnclr = Button(win, text = "Clear", bg = "Gray", command = self.clr)
        self.btnclr.place(x = 50, y = 200)
#add event-handling /bind () method

    def add(self,add):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END,str(result))

    def sub(self,sub):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1-num2
        self.txt3.insert(END, str(result))

    def ml(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))
    def div(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = round(num1 / num2, 3)
        self.txt3.insert(END, str(result))
    def clr(self):
        self.txt3.delete(0, 'end')
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()







