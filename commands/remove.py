def main(args, curs, conn):
    print(args)
    print(int(args[0]))
    if not args[0] or not int(args[0]):
        #if no content was specified
        raise ValueError("Primary key required as integer!")
    query = "DELETE FROM todos WHERE id=" + args[0]
    curs.execute(query)
    conn.commit()
    print("...Removed")
