
from contextlib import ContextDecorator
import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="postgres",
   user="postgres",
   password="Mddzcj12"
)

# read_dict: returns the list of all dictionary entries:
# argument: C - the database connection.

def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows

# add_word: executes to add a word to the list of all dictionary entries:
# argument: C, word, translation - the database connection, word and translation from table dictionary

def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()

# delete_word: executes to deletes the word inserted by finding the id of that word:
# argument: C, ID - the database connection and id in table.

def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()

# save_dict: returns the list of all dictionary entries to save:
# argument: C - the database connection.

def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close() 

list_of_commands = ("""Available list of commands: 
list   - list all words
add    - add a word to dictionary
delete - delete a word from dictionary
quit   - exit dictionary""") 

# print_help: returns the list of all commands available:
# argument: list_of_commands - the function with the list

def print_help():
    print(list_of_commands) 

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "help":
        print_help()
    elif cmd == "quit":
        save_dict(conn)
        exit()