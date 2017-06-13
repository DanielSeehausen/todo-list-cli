import sqlite3, sys

conn = sqlite3.connect('todos.db')
curs = conn.cursor()

if sys.version_info[0] < 3:
    print("You are not running this with Python3, which is what this has been tested on")
    # raise Exception("Python 3 or a more recent version is required.")

curs.execute('''CREATE TABLE todos
             (id INTEGER PRIMARY KEY, content TEXT, cat TEXT)''')

curs.execute("INSERT INTO todos(content, cat) VALUES(?, ?)", ['test content','test category'])
conn.commit()

print("\nCreated table: todos")
print("Either add todo_controller.py to environmental variables/path or alias it in bash profile.")
print("See list of available arg with:\n\t<alias/exec name> <help>")
