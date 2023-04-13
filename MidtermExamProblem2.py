from tkinter import *


# Code By Sergio, Jasper D.
class Name:
    # Widgets :D
    def __init__(self, win):
        self.title = Label(win, text="My Full name", font="CenturyGothic")
        self.title.place(x=250, y=20)
        self.l1 = Label(win, text="Enter given name", font="CenturyGothic")
        self.l1.place(x=100, y=100)
        self.in1 = Entry(win, borderwidth=1, width=30)
        self.in1.place(x=350, y=100)
        self.l2 = Label(win, text="Enter Middle name", font="CenturyGothic")
        self.l2.place(x=100, y=150)
        self.in2 = Entry(win, borderwidth=1, width=30)
        self.in2.place(x=350, y=150)
        self.l3 = Label(win, text="Enter Middle name", font="CenturyGothic")
        self.l3.place(x=100, y=200)
        self.in3 = Entry(win, borderwidth=1, width=30)
        self.in3.place(x=350, y=200)
        self.btn = Button(win, text="Show Full name", bg="Gray", command=self.fullname)
        self.btn.place(x=200, y=300)
        self.fl1 = Label(win, text="Full Name:", font="CenturyGothic")
        self.fl1.place(x=100, y=250)
        self.fl2 = Entry(win, bd=3, width=50)
        self.fl2.place(x=350, y=250)

    def fullname(self):
        self.fl2.delete(0, 'end')
        self.first = str(self.in1.get())
        self.middle = str(self.in2.get())
        self.last = str(self.in3.get())
        full = f"{self.first} {self.middle} {self.last}"  # Experimented on, using f"{variable}" works for tkinter
        self.fl2.insert(END, str(full))


window = Tk()
winn = Name(window)
window.geometry("700x500+20+20")
window.title("Midterm Exam Problem 2")
window.mainloop()
