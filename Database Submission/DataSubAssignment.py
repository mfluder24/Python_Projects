import sqlite3
# Connects to assignment.db 
conn = sqlite3.connect('assignment.db')
with conn:
    # Uses connection to create tbl_files, primary key, and column
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fname TEXT)")
    conn.commit()
# Closes connection to db
conn.close()

# Connects to assignment.db    
conn = sqlite3.connect('assignment.db')

# Tuple of file names
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# Looping through tuple objects to find .txt file names
for i in fileList:
    if i.endswith('txt'):
        with conn:
            cur = conn.cursor()
         # Each row's value will equal one item from tuple, therefore (i,) indicates
         # one element tuple for each filename ending with .txt
            cur.execute("INSERT INTO tbl_files (col_fname) VALUES (?)", (i,))
            print(i)
# Closes connection to db
conn.close
