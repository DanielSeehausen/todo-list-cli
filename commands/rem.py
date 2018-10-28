def main(args, curs, conn):
    try:
        row = curs.execute("SELECT * FROM todos WHERE id=?", [args[0]]).fetchall()[0]
        curs.execute("DELETE FROM todos WHERE id=?", [args[0]])
        conn.commit()
        print("\nDeleted: ", "|", row[0], "| " + row[2] + ' - ' + row[1])
    except:
        print("Need valid primary key as argument! `trem <id>`")
