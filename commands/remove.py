def main(args, curs, conn):
    if not args[0] or not int(args[0]): # TODO try catch on int coercion
        # asserting type and presence
        raise ValueError("Primary key required as integer!")
    row = curs.execute("SELECT * FROM todos WHERE id=?", [args[0]]).fetchall()[0]
    if row: # sqlite cant select and delete at once i believe (says this most efficient on interwebs)
        curs.execute("DELETE FROM todos WHERE id=?", [args[0]])
        conn.commit()
        print("\nDeleted: ", "|", row[0], "| " + row[2] + ' - ' + row[1])
    else:
        print("No matching row...doing nothing")


        # print_rows(curs.execute("SELECT * FROM todos WHERE cat=?", [args[0]]))
