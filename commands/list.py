import inspect

def print_rows(rows):
    for row in rows:
        print("|", row[0], "| " + row[2] + ' - ' + row[1])

def main(args, curs, conn):
    if len(args) > 0: # TODO add get specific cat
        all_results = curs.execute("SELECT * FROM todos ORDER BY cat ASC").fetchall()
    else:
        all_results = curs.execute("SELECT * FROM todos").fetchall()
    if not len(all_results):
        print("Nothing in todo list!")
    else:
        print_rows(all_results)
