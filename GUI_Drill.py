
import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(550, 165))
        self.master.title('Check files')
        self.master.config(bg='lightgray')


        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()


        self.txtFName = Entry(self.master,text=self.varBrowse1, font=("Helvetica", 12), fg='black', bg='white',width=40)
        self.txtFName.grid(row=0,column=1,columnspan=12, sticky=W+E+N+S,padx=(0,30), pady=(35,0))

        self.txtLName = Entry(self.master,text=self.varBrowse2, font=("Helvetica", 12), fg='black', bg='white',width=40)
        self.txtLName.grid(row=1,column=1,columnspan=12, sticky=W+E+N+S, padx=(0,30), pady=(10,0))

        self.btnClose = Button(self.master, text="Close Program", width=15, height=2)
        self.btnClose.grid(row=2,column=11,padx=(0,6), pady=(10,0), sticky=SE)

        self.btnBrowse = Button(self.master, text="Browse...", width=15, height=1)
        self.btnBrowse.grid(row=0,column=0,padx=(30,30), pady=(35,0), sticky=NW)

        self.btnBrowse = Button(self.master, text="Browse...", width=15, height=1)
        self.btnBrowse.grid(row=1,column=0,padx=(30,30), pady=(10,0), sticky=NW)

        self.btnF_Check = Button(self.master, text="Check for files...", width=15, height=2)
        self.btnF_Check.grid(row=2,column=0,padx=(30,30), pady=(10,0), sticky=NW)




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()






