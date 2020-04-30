import tkinter
from tkinter import filedialog
from tkinter import *

import os
path = 'C:\\py_drill'


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
        
        self.btnBrowse = Button(self.master, text="Browse Directory", width=15, height=1,command=self.move_dir)
        self.btnBrowse.grid(row=0,column=0,padx=(30,30), pady=(30,0), sticky=NW)

        self.btnBrowse = Button(self.master, text="Browse Directory", width=15, height=1,command=self.browse_button)
        self.btnBrowse.grid(row=1,column=0,padx=(30,30), pady=(30,0), sticky=NW)

        self.btnCancel = Button(self.master, text="Cancel", width=15, height=2,command=self.cancel)
        self.btnCancel.grid(row=2,column=0,padx=(30,30), pady=(30,0), sticky=NW)



        
    import os, shutil, pathlib, fnmatch
    def move_dir(self):
        if not os.path.isdir(dst):
            pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
            for f in fnmatch.filter(os.listdir(src), pattern):
                shutil.move(os.path.join(src, f), os.path.join(dst, f))


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
     

    

#_____________________________________________________________-

"""import sqlite3

conn = sqlite3.connect('drill_1.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fList\
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileN TEXT \
        )")
    conn.commit()



fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
with conn:
    for file in fileList:
        if file.endswith('.txt'):
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_fList(col_fileN) VALUES (?)", \
                (file,))
            print (file)"""








