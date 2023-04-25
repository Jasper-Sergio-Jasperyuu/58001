from tkinter import *
win = Tk()

win.geometry("500x400+10+10")
win.maxsize(500, 450)
win.minsize(500, 400)
l = Label(win, text="Gender")
l.place(relx=.45, rely=.45)
l.pack(anchor="center")
var1 = IntVar()
var2 = IntVar()
r1 = Radiobutton(win, text="male", variable=var1)
r1.place(x=25, y=25)
r2 = Radiobutton(win, text="female", variable=var2)
r2.place(x=25, y=45)

chk1 = Checkbutton(win, text="100-200")
chk2 = Checkbutton(win, text="201-300")
chk3 = Checkbutton(win, text="301-400")

chk1.place(x=25, y=70)
chk2.place(x=25, y=90)
chk3.place(x=25, y=110)

l2 = Label(win, text="List of Fruits")
l2.place(x=150, y=25)
lst = Listbox(win, selectmode="Single")
lst.insert(0, 'Mango')
lst.insert(1, 'Orange')
lst.insert(2, 'Banana')
lst.insert(3, 'Apple')

lst.place(x=150, y= 50)
win.mainloop()
