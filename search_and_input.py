
import psycopg2

connection = psycopg2.connect("dbname=ufc user=ufc")
cursor = connection.cursor()


print("U.F.C. DATABASE")

cursor.execute("SELECT * from ufc;")


def search_by_fighter():
    fighter_input = input("Search by fighter last name>>> ").capitalize()
    cursor.execute("SELECT * FROM ufc WHERE lastname = %s;", (fighter_input,))
    fetcher = (cursor.fetchall())
    printing = """
    rank: {}
    lastname: {}
    firstname: {}
    fights: {}
    strikes: {}
    tsac: {}
    td: {}
    tdac: {}
    kd: {}
    passes: {}
    rev: {}
    sub: {}
    """
    for result in fetcher:
        print(printing.format(*result))
    main_database()


def main_database():
    command = input("Type (ADD) to add fighter data, or (SEARCH) to search by name>>> ").lower()
    if command == "add":
        print("Input fighter stats")
        rank = input("rank>>> ")
        lastname = input("last name>>> ")
        firstname = input("first name>>> ")
        fights = input("fights>>> ")
        strikes = input("strikes>>>")
        tsac = input("total strike accuracy>>> ")
        td = input("takedowns>>> ")
        tdac = input("takedown aaccuracy>>> ")
        kd = input("knock downs>>> ")
        passes = input("passes>>> ")
        rev = input("reversals>>> ")
        sub = input("submissions>>> ")
        cursor.execute("INSERT INTO ufc VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (rank, lastname, firstname, fights, strikes, tsac, td, tdac, kd, passes, rev, sub))
        connection.commit()
        print("Data added")
        main_database()

    elif command == "search":
        search_by_fighter()
    else:
        print("please choose 'ADD', or 'SEARCH'")
        main_database()


main_database()

cursor.execute


connection.commit()

cursor.close()
connection.close()
