
import psycopg2

# Write a program that connects to the database and
# asks the user to search for a player
#  Start with just the name but think about
#  further criteria you could include (position? age?).
#   For a given result set, have the program display the
#    results in a clean manner to the user.
#
# Add a feature to your program that allows a
# user to insert new players into the database.
# Prompt the user for every column that you
#  will need them to provide custom information on.
# Name?, Age?, etc.

connection = psycopg2.connect("dbname=ufc user=ufc")
cursor = connection.cursor()


print("U.F.C. DATABASE")

cursor.execute("SELECT * from ufc;")


def search_by_fighter():
    fighter_input = input("Search by fighter last name>>> ").capitalize()
    cursor.execute("SELECT * FROM ufc WHERE lastname = %s;", (fighter_input,))
    fetcher = (cursor.fetchall())
    # print(fetcher)
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
        # for i in result:
        print(printing.format(*result))


def main_database():
    command = input("Type (ADD) to add fighter data, or (SEARCH) to search by name>>> ").lower()
    if command == "add":
        print("Input fighter stats")
        rank = input("rank>>> ")
        lastname = input("last name>>> ")
        firstname = input("first name>>> ")
        fights = input("fights>>> ")
        strikes = input("strikes")
        tsac = input("total strike accuracy>>> ")
        td = input("takedowns>>> ")
        tdac = input("takedown aaccuracy>>> ")
        kd = input("knock downs>>> ")
        passes = input("passes>>> ")
        rev = input("reversals>>> ")
        sub = input("submissions>>> ")
        cursor.execute("INSERT INTO ufc VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (rank, lastname, firstname, fights, strikes, tsac, td, tdac, kd, passes, rev, sub))
        print("Data added")

    elif command == "search":
        search_by_fighter()
    else:
        print("please choose 'ADD', or 'SEARCH'")
        main_database()


main_database()

cursor.execute

# cursor.execute("INSERT INTO ufc VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#                    (row["RANK"], row["LASTNAME"], row["FIRSTNAME"], row["FIGHTS"], row["STR"],
#                     row["TSAC"], row["TD"], row["TDAC"], row["KD"], row["PASS"], row["REV"], row["SUB"]))

connection.commit()
cursor.close()
connection.close()
