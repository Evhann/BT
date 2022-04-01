# background='#1e1e1e', foreground='#ffffff'
# bar #333333
# other #7a838e
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class pIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("pIDE") # Window title
        self.root.geometry("1280x720") # Window default size
        self.filename = str()
        self.title = StringVar()

        self.filetypes = (("All Files","*.*"),("""Text Files (*.txt)""","*.txt"),("""Python Files ("*.py", "*.pyw", "*.py3", "*.pxd", "*.pyx", "*.ipynb")""",("*.py", "*.pyw", "*.py3", "*.pxd", "*.pyx", "*.ipynb")), ("""C files ("*.c", "*.h")""", ("*.c", "*.h")), ("""Ren'py files (*.rpy)""", "*.rpy"), ("""Markdown files (*.md)""", "*.md"), ("""Config file ("*.ini")""", "*.ini"))

        self.titlebar = Label(self.root, textvariable=self.title, font=("Arial", 12), bd=2, relief=GROOVE, bg='#7a838e')
        self.titlebar.pack(side=TOP, fill=BOTH)
        self.settitle()
        

        self.menubar = Menu(self.root, font=("Segoe UI",16), activebackground="skyblue", bg='#333333') # Menu bar at the top of the screen
        self.root.config(menu=self.menubar)
        
        self.filemenu = Menu(self.menubar,font=("Segoe UI",11),activebackground="skyblue",tearoff=0)
        self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
        self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
        self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
        self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
        
        self.menubar.add_separator()
        
        self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        
        self.editmenu = Menu(self.menubar,font=("Segoe UI",11),activebackground="skyblue",tearoff=0)
        self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
        self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
        self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
        
        self.editmenu.add_separator()
        
        self.editmenu.add_command(label="Undo",accelerator="Ctrl+Z",command=self.undo)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.helpmenu = Menu(self.menubar,font=("Segoe UI",11),activebackground="skyblue",tearoff=0)
        self.helpmenu.add_command(label="About",command=self.infoabout)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        
        scrol_y = Scrollbar(self.root,orient=VERTICAL)
        self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("Consolas",13, "bold"),state="normal",relief=GROOVE, background='#1e1e1e', foreground='#ffffff')
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        self.shortcuts()
    
    def settitle(self):
        if self.filename:
            self.title.set(self.filename)
        else:
            self.title.set("Untitled")
    
    def newfile(self, *args):
        self.txtarea.delete("1.0", END)
        self.filename = None
        self.settitle()

    
    def openfile(self, *args):
        try:
            self.filename = filedialog.askopenfilename(title = "Select file",filetypes = self.filetypes)
            if self.filename:
                infile = open(self.filename,"r")
                self.txtarea.delete("1.0",END)
                for line in infile:
                    self.txtarea.insert(END,line)
                
                infile.close()
                self.settitle()

        except Exception as e:
            messagebox.showerror("Exception", e)
    
    def savefile(self,*args):
        # Exception handling
        try:

            if self.filename:
                data = self.txtarea.get("1.0",END)
                outfile = open(self.filename,"w")
                outfile.write(data)
                outfile.close()
                self.settitle()

            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror("Exception", e)
    
    def saveasfile(self,*args):
        # Exception handling
        try:

            untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = self.filetypes)
            data = self.txtarea.get("1.0",END)
            outfile = open(untitledfile,"w")
            outfile.write(data)
            outfile.close()
            self.filename = untitledfile
            self.settitle()

        except Exception as e:
            messagebox.showerror("Exception", e)
    def exit(self,*args):
        op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!")
        if op>0:
                self.root.destroy()
        else:
            return
    def cut(self,*args):
        self.txtarea.event_generate("<<Cut>>")

    def copy(self,*args):
        self.txtarea.event_generate("<<Copy>>")


    def paste(self,*args):
        self.txtarea.event_generate("<<Paste>>")


    def undo(self, *args):
        try:
            if self.name:
                self.txtarea.delete("1.0", END)
                infile = open(self.filename, 'r')
                for line in infile:
                    self.txtare.insert(END, line)
                
                infile.close()
                self.settitle()

            else:
                self.txtare.delete("1.0", END)
                self.filename = None
                self.settitle()

        except Exception as e:
            messagebox.showerror("Exception", e)
    
    def infoabout(self):
        from os.path import dirname
        dn = dirname(__file__)
        if dn[-3:] != 'src':
            from os import chdir
            chdir('src')
            import about
        else:
            import about

    def shortcuts(self):
        # Binding Ctrl+n to newfile funtion
        self.txtarea.bind("<Control-n>",self.newfile)
        # Binding Ctrl+o to openfile funtion
        self.txtarea.bind("<Control-o>",self.openfile)
        # Binding Ctrl+s to savefile funtion
        self.txtarea.bind("<Control-s>",self.savefile)
        # Binding Ctrl+a to saveasfile funtion
        self.txtarea.bind("<Control-a>",self.saveasfile)
        # Binding Ctrl+e to exit funtion
        self.txtarea.bind("<Control-e>",self.exit)
        # Binding Ctrl+x to cut funtion
        self.txtarea.bind("<Control-x>",self.cut)
        # Binding Ctrl+c to copy funtion
        self.txtarea.bind("<Control-c>",self.copy)
        # Binding Ctrl+v to paste funtion
        self.txtarea.bind("<Control-v>",self.paste)
        # Binding Ctrl+z to undo funtion
        self.txtarea.bind("<Control-z>",self.undo)

root = Tk()
pIDE(root)
root.mainloop()

