import tkinter
from tkinter import filedialog
from tkinter import *



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(550, 200))
        self.master.title('Check files')
        self.master.config(bg='lightgray')

       
        self.lbl1 = Label(master=root,textvariable=folder_path,font=("Helvetica"), fg='black', bg='lightgray',width=40)
        self.lbl1.grid(row=0,column=1,columnspan=12, sticky=W+E+N+S,padx=(0,30), pady=(35,0))
        
        self.btnBrowse = Button(self.master, text="Browse Directory", width=15, height=1,command=self.browse_button)
        self.btnBrowse.grid(row=0,column=0,padx=(30,30), pady=(30,0), sticky=NW)

        self.btnCancel = Button(self.master, text="Cancel", width=15, height=2,command=self.cancel)
        self.btnCancel.grid(row=2,column=0,padx=(30,30), pady=(0,0), sticky=NW)

        
       


    def browse_button(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        global folder_path
        filename = filedialog.askdirectory()
        folder_path.set(filename)
        print(filename)

    def cancel(self):
        self.master.destroy()



if __name__ == "__main__":
    root = Tk()
    folder_path = StringVar()
    App = ParentWindow(root)
    root.mainloop()
     
