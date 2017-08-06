import logging
import sqlite3


class SqlUtils(object):
    def __init__(self):
        self.db_path = '..\\db\\account.db'
        self.ticket_table_name = 'tickets'
        self.coal_table_name = 'coals'
        self.record_by_car_table_name = 'record_by_car_detail'

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        return conn

    def close_connection(self, conn):
        if conn is not None:
            conn.close()

    def create_ticket_table_if_necessary(self, cursor):
        create_table_sql = '''CREATE TABLE IF NOT EXISTS %s
                     (DATE TEXT NOT NULL,
                      TICKET_NAME TEXT PRIMARY KEY,
                      PURCHASE_PRICE REAL, 
                      PURCHASE_COMPUTE_WAY TEXT,
                      SELL_PRICE REAL,
                      SELL_COMPUTE_WAY TEXT)''' % self.ticket_table_name
        logging.info(create_table_sql)
        cursor.execute(create_table_sql)

    def create_coal_table_if_necessary(self, cursor):
        create_coal_table_sql = '''CREATE TABLE IF NOT EXISTS %s 
                                (DATE TEXT NOT NULL,
                                 COAL_NAME TEXT PRIMARY KEY,
                                 PURCHASE_PRICE REAL,
                                 PURCHASE_COMPUTE_WAY TEXT,
                                 SELL_PRICE REAL,
                                 SELL_COMPUTE_WAY TEXT)''' % self.coal_table_name
        logging.info(create_coal_table_sql)
        cursor.execute(create_coal_table_sql)

    def create_record_by_car_detail_table_if_necessary(self, cursor):
        create_table_sql = '''CREATE TABLE IF NOT EXISTS %s 
                                (DATE TEXT NOT NULL,
                                 PERSON_NAME TEXT NOT NULL,
                                 CAR_ID TEXT,
                                 COAL_NAME TEXT,
                                 WEIGHT_VALUE REAL,
                                 TICKET_NAME TEXT)''' % self.record_by_car_table_name
        logging.info(create_table_sql)
        cursor.execute(create_table_sql)

    def delete_table(self, table_name, cursor):
        sql = 'DROP TABLE ' + table_name
        cursor.execute(sql)

    def add_ticket_record(self, add_date, ticket_name, purchase_compute_way, purchase_price,
                          sell_compute_way, sell_price):
        conn = self.get_connection()
        cursor = conn.cursor()
        record = (add_date, ticket_name, purchase_price, purchase_compute_way, sell_price, sell_compute_way)
        sql = 'insert into %s values(?,?,?,?,?,?)' % self.ticket_table_name
        logging.info("execute sql:" + sql)
        cursor.execute(sql, record)
        conn.commit()
        conn.close()
        # 原子性???

    def add_coal_record(self, add_date, coal_name, purchase_compute_way, purchase_price,
                        sell_compute_way, sell_price):
        conn = self.get_connection()
        cursor = conn.cursor()
        record = (add_date, coal_name, purchase_price, purchase_compute_way, sell_price, sell_compute_way)
        sql = 'INSERT INTO %s VALUES(?,?,?,?,?,?)' % self.coal_table_name
        logging.info("execute sql:" + str(sql))
        cursor.execute(sql, record)
        conn.commit()
        conn.close()

        # 原子性???

    def add_record_by_car_detail(self, date, person_name, car_id, coal_name, weight_value, ticket_name):
        conn = self.get_connection()
        cursor = conn.cursor()
        record_by_car = (date, person_name, car_id, coal_name, weight_value, ticket_name)
        logging.info("record info is ", record_by_car)
        sql = 'INSERT INTO %s VALUES(?,?,?,?,?,?)' % self.record_by_car_table_name
        logging.info("execute sql:" + sql)
        cursor.execute(sql, record_by_car)
        conn.commit()
        conn.close()

    def query_all_tickets_name(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT TICKET_NAME FROM %s' % self.ticket_table_name
        logging.info("execute sql:" + sql)
        cursor.execute(sql)
        fetch_result = cursor.fetchall()
        logging.info(fetch_result)
        conn.close()
        return fetch_result

    def query_all_coal_names(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = 'SELECT COAL_NAME FROM %s' % self.coal_table_name
        logging.info("execute sql:" + sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        logging.info(results)
        conn.close()
        return results


if __name__ == '__main__':
    sqlUtils = SqlUtils()
    # sqlUtils.delete_table('coals')
    sqlUtils.add_coal_record('2017/08/05', '面煤', 'bytons', '324', 'bytons', '336')
    # sqlUtils.add_record_by_car_detail('2017/08/05', 'fff', 'fff', '面煤', '2.00', '北线')
    # sqlUtils.query_all_tickets_name()
    print(sqlUtils.query_all_coal_names())
    # date = time.strftime('%Y/%m/%d', time.localtime(time.time()))  # 当前时间
    # print(date, type(date))
    # sqlUtils.delete_table('tickets')
