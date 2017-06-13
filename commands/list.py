import inspect

def print_rows(rows):
    for row in rows:
        print("|", row[0], "| " + row[2] + ' - ' + row[1])


def main(args, curs, conn):
    if len(args) > 0:
        print_rows(curs.execute("SELECT * FROM todos WHERE cat=?", [args[0]]))
    else:
        all_results = curs.execute("SELECT * FROM todos").fetchall()
        if not len(all_results):
            print("Nothing in todo list!")
        else:
            print_rows(all_results)
