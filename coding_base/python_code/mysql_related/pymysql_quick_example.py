#!/usr/bin/env python
import pymysql


class mysql_db(object):
    def __init__(self, db_info):
        self.host, self.user, self.password = db_info.split()
        self.connection = None
        print(self.host, self.user, self.password)
    """
    build datebase connection
    """

    def connect(self):
        self.connection = pymysql.connect(self.host, self.user, self.password)

    """
    get all the table names
    """

    def get_table_names(self):
        # build datebase connection
        self.connect()

        # select all the table names
        sql = "select table_name from information_schema.tables limit 10"
        curs = self.connection.cursor()
        curs.execute(sql)
        table_names = set(x[0] for x in curs.fetchall())

        # close cursor and database connection
        curs.close()
        self.connection.close()

        return table_names


# test
db_info = "localhost root root123"
test = mysql_db(db_info)
test.connect()
print(test.get_table_names())
