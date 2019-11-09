from tkinter import *

root = Tk()

e = Entry(root, width=20)
b = Button(root, text="Just a Button")
l = Label(root, bg='black', fg='white', width=20)

def str_to_list(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

b.bind('<Button-1>', str_to_list)

e.pack()
b.pack()
l.pack()

root.mainloop()
