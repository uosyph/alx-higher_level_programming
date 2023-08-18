#!/usr/bin/python3
"""Lists all states with a name starting with N"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    db.close()

    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")
