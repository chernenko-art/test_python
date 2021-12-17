import mysql.connector
from model.group import Group
from model.user import User


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password,
                                                  autocommit=True)  # autocommit - clear cache after connect

    def destroy(self):
        self.connection.close()

    # extract Group data from db
    def get_group_list(self):
        list = []  # list for extracted Group
        cursor = self.connection.cursor()  # method for get data from database
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                id, name, header, footer = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    # extract User data from db
    def get_user_list(self):
        list = []  # list for extracted Group
        cursor = self.connection.cursor()  # method for get data from database
        try:
            cursor.execute("select id, firstname, lastname, middlename from addressbook  where deprecated is NULL")
            for row in cursor:
                id, firstname, lastname, middlename = row
                list.append(User(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename))
        finally:
            cursor.close()
        return list
