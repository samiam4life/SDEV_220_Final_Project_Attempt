import sqlite3
 
# connecting to the database
connection = sqlite3.connect("gfg.db")
 
# cursor
crsr = connection.cursor()

crsr.execute('''DROP TABLE dice;''')
connection.commit()
 
# SQL command to create a table in the database
sql_command = """CREATE TABLE dice ( 
dice_num INTEGER PRIMARY KEY, 
dice_name VARCHAR(20), 
dice_price INTEGER, 
dice_inventory INTEGER,
dice_backstock INTEGER, 
last_ordered_dice DATE);"""
 
# execute the statement
crsr.execute(sql_command)

# primary key
d_pk = [101,102,103,104,105,106,107,108,109,110]
 
# Enter 5 students first names
dice_name = ['Dragon Dice', 'Galaxy Dice', 'Mini Silver Dice', 'Black Metal Dice', 'Jumbo Red D20', 'Rainbow Dice', "Mini Rainbow Dice",
             'Green and Gold Metal Dice', 'Blue Liquid Core Dice', 'Flower Dice' ]
 
# Enter 5 students last names
dice_price = ['15.00','20.99','25.50','35.99','40.00','22.50','17.00','45.00','40.99','18.99']
 
# Enter their gender respectively
dice_inventory = ['10','7','9','5','10','2','1','8','10','6']

dice_backstock = ['20','15','3','9','0','10','16','4','20','0']
 
# Enter their joining data respectively
last_ordered_dice = ['2023-12-02', '2023-11-26', '2023-10-14', '2023-10-14', '2023-10-14','2023-10-21','2023-11-26','2023-09-30','2023-12-02',
                '2023-09-30']
 
for i in range(10):
 
    # This is the q-mark style:
     crsr.execute('INSERT INTO dice VALUES (?, ?, ?, ?, ?, ?)', 
               (d_pk[i], dice_name[i], dice_price[i], dice_inventory[i], dice_backstock[i], last_ordered_dice[i]))

 
# close the connection

connection.commit()
crsr.execute("SELECT * from dice")
ans = crsr.fetchall()
for i in ans:
    print(i)

connection.close()