import sqlite3
import time


class SqlUtils(object):
    def __init__(self):
        self.conn = sqlite3.connect('..\\db\\account.db')
        self.cursor = self.conn.cursor()

    def create_ticket_table_if_necessary(self):
        self.cursor.execute('''CREATE TABLE if not exists tickets
                     (date text, ticket_name text, purchase_price real, 
                     purchase_compute_way text, sell_price real, sell_compute_way)''')

    def delete_table(self, table_name):
        sql = 'DROP TABLE ' + table_name
        self.cursor.execute(sql)
        self.tear_down()

    def add_ticket_record(self, ticket_name, purchase_compute_way, purchase_price, sell_compute_way, sell_price):
        self.create_ticket_table_if_necessary()
        date = time.strftime('%Y/%m/%d', time.localtime(time.time()))  # 当前时间
        record = (date, ticket_name, purchase_price, purchase_compute_way, sell_price, sell_compute_way)
        sql = 'insert into tickets values(?,?,?,?,?,?)'
        self.cursor.execute(sql, record)
        self.tear_down()

    def query_all_ticket_record(self):
        sql = 'select * from tickets'
        self.cursor.execute(sql)
        print(self.cursor.fetchall())

    def tear_down(self):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    # sqlUtils = SqlUtils()
    # sqlUtils.add_ticket_record('example1', '1.2', 'bytons', '1.2', 'bycars')
    # sqlUtils.query_all_ticket_record()
    date = time.strftime('%Y/%m/%d', time.localtime(time.time()))  # 当前时间
    print (date, type(date))
    # sqlUtils.delete_table('tickets')
