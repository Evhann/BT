from tkinter import *


aboutScreen = Tk()
aboutScreen.geometry("640x480")
aboutScreen.title("About pIDE")
aboutScreen.configure(bg='#1e1e1e')

t = Label(master=aboutScreen, text="This section isn't complete.", font=("Segoe UI", 16), bg='#1e1e1e', foreground='#ffffff')
t.pack()

aboutScreen.mainloop()