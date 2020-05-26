import sqlite3
import sys
import easygui

class myDatabase:
    try:
        def __init__(self):
            try:
                self.dates = []
                self.connection = sqlite3.connect('myDB.db')     #set up connection to DB
                self.cursor = self.connection.cursor()   #create cursor object
                # print (self.connection.get_dsn_parameters(),"\n")
            except:
                image = "Ops.jpg"
                response = easygui.buttonbox(msg='Database has not been connected...', title='Oops, something is wrong', image= image, choices = ('Try again', 'Close'))
                if response == "Close":
                    sys.exit(0)
                if response == "Try again":
                    self.__init__()

        def addToDatabase(self, date_value, time_value, activity_value):
            insert_query = f"INSERT INTO activity (date, time, activity) VALUES('{date_value}', '{time_value}', '{activity_value}')"
            self.cursor.execute(insert_query)
            self.connection.commit()


        def getFromDatabase(self, table):  # get
            list_of_quotes = []
            self.cursor.execute(f"SELECT * FROM {table}")
            for row in self.cursor:
                list_of_quotes.append(row)
            return list_of_quotes


        def doneUpdateDatabase(self, table, value1, value2, value3):  # activity is done
            new_value = value3 + "-DONE"  # add 'done' to activity
            self.cursor.execute(
                f"UPDATE {table} SET activity = '{new_value}' WHERE date = '{value1}' AND time = '{value2}' AND activity = '{value3}'")
            self.connection.commit()


        def deleteFromDatabase(self, table, value1, value2, value3):  # delete an activity
            self.cursor.execute(f"DELETE FROM {table} WHERE date = '{value1}' AND time = '{value2}' AND activity = '{value3}'")
            self.connection.commit()

    except sqlite3.DatabaseError:
        print('Error in DB')
        sys.exit(0)


# db1 = myDatabase()
# newDB.addToDatabase('12.31.2020', '11:00', 'swimming')
# insert into activity values ('12.31.2020', '10:00', 'running');

