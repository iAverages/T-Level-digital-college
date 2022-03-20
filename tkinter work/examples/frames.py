from tkinter import *

ws = Tk()
ws.title('Python Guides')
ws.geometry('250x200')

frame1 = Frame(ws, padx=5, pady=5)
frame1.grid(row=0, column=1)

Label(frame1, text='Name', padx=5, pady=5).pack()
Label(frame1, text='Email', padx=5, pady=5).pack()
Label(frame1, text='Password', padx=5, pady=5).pack()
 

frame2 = Frame(ws, padx=5, pady=5)
frame2.grid(row=0, column=2)

Entry(frame2).pack(padx=5, pady=5)
Entry(frame2).pack(padx=5, pady=5)
Entry(frame2).pack(padx=5, pady=5)


Button(ws, text='Submit', padx=10).grid(row=1, columnspan=5, pady=5)


ws.mainloop()
