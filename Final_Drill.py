import tkinter
from tkinter import filedialog
from tkinter import *
import os, shutil, pathlib, fnmatch
import time
import sqlite3




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


        self.btnBrowse = Button(self.master, text="Browse...", width=15, height=1, command=self.picSrc_dir)
        self.btnBrowse.grid(row=0,column=0,padx=(30,30), pady=(35,0), sticky=NW)

        self.btnBrowse = Button(self.master, text="Browse...", width=15, height=1, command=self.dest_dir)
        self.btnBrowse.grid(row=1,column=0,padx=(30,30), pady=(10,0), sticky=NW)

        self.btnF_Check = Button(self.master, text="Check for files...", width=15, height=2, command=self.moveFiles)
        self.btnF_Check.grid(row=2,column=0,padx=(30,30), pady=(10,0), sticky=NW)

        self.btnClose = Button(self.master, text="Close Program", width=15, height=2, command=self.cancel)
        self.btnClose.grid(row=2,column=11,padx=(0,6), pady=(10,0), sticky=SE)




    conn = sqlite3.connect('drill_final.db')

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_fList\
            (ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileN TEXT \
            )")
        



        
    
    def moveFiles(self):
        source=self.txtFName.get()
        dest=self.txtLName.get()
        sourcefiles=os.listdir(source)
        for file in sourcefiles:
            if fnmatch.fnmatch(file, '*.txt'):
                abPath = os.path.join(source,file)
                fTime = os.path.getmtime(abPath)
                local_time = time.ctime(fTime)
                print (file,local_time)
                shutil.move(abPath,dest)
                with conn:
                    cur.execute("INSERT INTO tbl_fList(col_fileN) VALUES (?)",(file,))
                    conn.commit()
    
                    
                
        


    def picSrc_dir(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        filename = filedialog.askdirectory()
        self.txtFName.delete(0,END)
        self.txtFName.insert(0,filename)
        

    def dest_dir(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        filename = filedialog.askdirectory()
        self.txtLName.delete(0,END)
        self.txtLName.insert(0,filename)


    
        
        

    def cancel(self):
        self.master.destroy()



if __name__ == "__main__":
    root = Tk()
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








