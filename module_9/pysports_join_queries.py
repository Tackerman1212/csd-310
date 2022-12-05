# Tanner Ackerman
# Assignment: PySports: Basic Table Joins


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


try:

    database = mysql.connector.connect(**config) 

    cursor = database.cursor()

# This line is the main difference between this and the previous queries assignment.
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players_table = cursor.fetchall()

    print("\n")
    print("-- DISPLAYING PLAYER RECORDS --")

    for player in players_table:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    print("\n\n")
    input(" Press any key to continue... ")
    print("\n")

# noticed this is similar to the queries assignment last week.

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:

    db.close()