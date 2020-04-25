import sqlite3

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
            print (file)
            

    


