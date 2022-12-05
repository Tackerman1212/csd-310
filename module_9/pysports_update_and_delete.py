# Tanner Ackerman
# Assignment: PySports: Update and Delete
# Module: 9


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def display(cursor, title):

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    players = cursor.fetchall()

    print("\n")
    print("{}".format(title))

    for player in players:
        print("Player ID: {} \n First Name: {} \n Last Name: {} \n Team Name: {} \n".format(player[0],player[1],player[2],player[3]))



try:

    database = mysql.connector.connect(**config)

    cursor = database.cursor()
    
    # inserted a new record into the player table for Team Gandalf
    insert = ("INSERT INTO player(first_name, last_name, team_id)" "VALUES(%s, %s, %s)")
    
    value = ("Smeagol", "Shire Folk", 1)
    
    cursor.execute(insert, value)

    database.commit()

    display(cursor, " -- DISPLAYING PLAYERS AFTER INSERT -- ")



    # updated the newly inserted record by changing the player's team to Team Sauron or "team_id" = 2
    update = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute(update)
    
    display(cursor, " -- DISPLAYING PLAYERS AFTER UPDATE -- ")
    
   

   # executed a delete query to remove the updated record
    delete = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete)

    display(cursor, " -- DISPLAYING PLAYERS AFTER DELETE -- ")

    
    input("\n Press any key to continue... ")


except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)


finally:
    
    database.close()
