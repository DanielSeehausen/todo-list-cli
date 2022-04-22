#!/usr/bin/env python3

import os, sys, importlib, glob

'''
This is the entry point and work horse of the program
The first sys.argv is handled at the controller level (i.e. what action you want [list, add, remove, etc.])
This was a very quick project to cram my todolist onto the CLI, and minimal error handling/improper argument handling has been provided.
'''

# TODO better way of doing this
dname = os.path.dirname(os.path.abspath(__file__))
os.chdir(dname)
sys.path.append(os.path.join(os.path.dirname(__file__), "./commands"))

def print_help():
    print("\tadd <content> <category[optional]>")
    print("\trem <row_id>")
    print("\tprint_db")
    print("\tlist <category[optional]>")

def create_table_if_absent(curs):
    curs.execute('''CREATE TABLE IF NOT EXISTS todos
                 (id INTEGER PRIMARY KEY, content TEXT, cat TEXT)''')

def execute_command(args):
    import sqlite3
    conn = sqlite3.connect('todos.db')
    curs = conn.cursor()
    create_table_if_absent(curs)

    # function dispatch: passes all args to the resolved function
    command = importlib.import_module(args[0]).main
    com_args = None if len(args) < 1 else args[1:]
    command(com_args, curs, conn)

def get_all_commands():
    # commands are resolved from file names! jank to the max BB
    return [x.split('/')[-1][:-3:] for x in glob.iglob('./commands/*.py')]

def main(args):
    if args[0] == 'help' or args[0] == '-h':
        print_help()
    elif args[0] not in get_all_commands():
        print("Command not recognized. Try:")
        print_help()
    else:
        execute_command(args)

# Entry point. If no arguments provided returns after printing some meatbag help
if len(sys.argv) > 1:
    main(sys.argv[1:])
else:
    print("Provide a command:")
    print_help()
