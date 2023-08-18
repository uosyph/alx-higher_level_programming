#!/usr/bin/python3
"""Lists all states where name matches argument"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute(f'SELECT *\
                FROM states\
                WHERE states.name LIKE BINARY "{str(argv[4])}"\
                ORDER BY states.id ASC')
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"{row}")

    cur.close()
    db.close()
