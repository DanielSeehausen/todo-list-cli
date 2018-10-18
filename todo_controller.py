#!/usr/bin/env python3

import os, sys, importlib, glob

'''
This is the main entry point and work horse of the program once the database has been created
The first two sys.argvs (filename.py, action/command) are handled at the controller level
All arguments beyond those two are handled by the action/command that is being invoked (they use varying quantities of args)
This was a very quick project to cram my todolist onto the CLI, and minimal error handling/improper argument handling has been provided.
'''

# TODO better way of doing this
dname = os.path.dirname(os.path.abspath(__file__))
os.chdir(dname)
sys.path.append(os.path.join(os.path.dirname(__file__), "./commands"))

def print_help():
    print("\nCommands available (* denotes optional):")
    print("\tadd <content> <category>*")
    print("\tremove <row_id of row>")
    print("\tprint_db")
    print("\tlist <cat>* (defaults to listing all)")

def get_all_commands():
    return [x.split('/')[-1][:-3:] for x in glob.iglob('./commands/*.py')]

def command_not_found():
    print("Command not recognized.\nCommands available: ")
    for command in get_all_commands():
        print("\t" + command)

def execute_command(args):
    if not args[0]:
        raise ValueError("Missing <command> argument!")
    import sqlite3
    conn = sqlite3.connect('todos.db')
    curs = conn.cursor()
    command = importlib.import_module(args[0]).main
    com_args = None if len(args) < 1 else args[1:]
    command(com_args, curs, conn)

def main(args):
    all_commands = get_all_commands()
    if args[0] is 'help':
        print_help()
    elif args[0] not in all_commands:
        command_not_found()
    else:
        execute_command(args)

if len(sys.argv) > 1:
    main(sys.argv[1:])
else:
    command_not_found()
