#DEPRECATED -- does not provide any functionality beyond list
def main(args, curs, conn):
    for row in curs.execute("SELECT * FROM todos"):
        print(row)
