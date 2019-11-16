from tkinter import *

root = Tk()

e = Entry(root, width=40, bg = 'blue')
b = Button(root, text="Sort", width=29, bg = 'red', font = 'Arial 10')
l = Label(root, bg='black', fg='white', width=34)

root.title('Sorter')
root.geometry('250x200')

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
