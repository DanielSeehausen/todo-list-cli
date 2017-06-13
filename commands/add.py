# import time

def main(args, curs, conn):
    if not args[0]:
        #if no content was specified
        raise ValueError("Content must have a value!")
    if len(args) == 1:
        #if no category was given, default to gen category
        args.append('gen')
    # date = time.strftime("%H:%M:%S")
    query = "INSERT INTO todos(content, cat) VALUES(?, ?)"
    values = [args[0], args[1]]
    curs.execute(query, values)
    conn.commit()
    print("...added")
