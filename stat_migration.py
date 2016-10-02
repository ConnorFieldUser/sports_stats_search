import psycopg2

from sports_search import stats

connection = psycopg2.connect("dbname=ufc user=ufc")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS ufc;")

create_table_command = """
CREATE TABLE ufc (
    RANK serial PRIMARY KEY,
    LASTNAME VARCHAR(20),
    FIRSTNAME VARCHAR(20),
    FIGHTS NUMERIC(2),
    STR NUMERIC(4),
    TSAC VARCHAR(9),
    TD NUMERIC(4),
    TDAC VARCHAR(9),
    KD NUMERIC(4),
    PASS NUMERIC(4),
    REV NUMERIC(4),
    SUB NUMERIC(3)
);
"""

cursor.execute(create_table_command)

for row in stats:
    cursor.execute("INSERT INTO ufc VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (row["RANK"], row["LASTNAME"], row["FIRSTNAME"], row["FIGHTS"], row["STR"],
                    row["TSAC"], row["TD"], row["TDAC"], row["KD"], row["PASS"], row["REV"], row["SUB"]))

connection.commit()
cursor.close()
connection.close()
