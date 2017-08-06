import sqlite3


class SqlUtils(object):
    def __init__(self):
        self.db_path = '..\\db\\account.db'
        self.ticket_table_name = 'tickets'
        self.coal_table_name = 'coals'
        self.record_by_car_table_name = 'record_by_car_detail'

    def create_ticket_table_if_necessary(self, cursor):
        create_table_sql = '''CREATE TABLE if not exists %s
                     (date text, ticket_name text, purchase_price real, 
                     purchase_compute_way text, sell_price real, sell_compute_way text)''' \
                           % self.ticket_table_name
        print(create_table_sql)
        cursor.execute(create_table_sql)

    def create_coal_table_if_necessary(self, cursor):
        create_coal_table_sql = 'CREATE TABLE if not exists %s ' \
                                '(date text, coal_name text, purchase_price real, purchase_compute_way text, sell_price real,' \
                                'sell_compute_way text)' % self.coal_table_name
        print(create_coal_table_sql)
        cursor.execute(create_coal_table_sql)

    def create_record_by_car_detail_table_if_necessary(self, cursor):
        create_table_sql = 'CREATE TABLE if not exists %s ' \
                           '(date text, person_name text, car_id text, coal_name text, weight_value real,' \
                           'ticket_name text)' % self.record_by_car_table_name
        print(create_table_sql)
        cursor.execute(create_table_sql)

    def delete_table(self, table_name):
        ops = self.pre_ops()
        conn = ops[0]
        cursor = ops[1]
        sql = 'DROP TABLE ' + table_name
        cursor.execute(sql)
        self.post_ops(conn)

    def add_ticket_record(self, add_date, ticket_name, purchase_compute_way, purchase_price,
                          sell_compute_way, sell_price):
        ops = self.pre_ops()
        conn = ops[0]
        cursor = ops[1]
        self.create_ticket_table_if_necessary(cursor)
        record = (add_date, ticket_name, purchase_price, purchase_compute_way, sell_price, sell_compute_way)
        sql = 'insert into %s values(?,?,?,?,?,?)' % self.ticket_table_name
        print("execute sql:", sql)
        cursor.execute(sql, record)
        # 原子性???
        self.post_ops(conn)

    def add_coal_record(self, add_date, coal_name, purchase_compute_way, purchase_price,
                        sell_compute_way, sell_price):
        ops = self.pre_ops()
        conn = ops[0]
        cursor = ops[1]
        self.create_ticket_table_if_necessary(cursor)
        record = (add_date, coal_name, purchase_price, purchase_compute_way, sell_price, sell_compute_way)
        sql = 'insert into %s values(?,?,?,?,?,?)' % self.coal_table_name
        print("execute sql:", sql)
        cursor.execute(sql, record)
        # 原子性???
        self.post_ops(conn)

    def add_record_by_car_detail(self, date, person_name, car_id, coal_name, weight_value, ticket_name):
        ops = self.pre_ops()
        conn = ops[0]
        cursor = ops[1]
        self.create_record_by_car_detail_table_if_necessary(cursor)
        record_by_car = (date, person_name, car_id, coal_name, weight_value, ticket_name)
        print("record info is ", record_by_car)
        sql = 'insert into %s values(?,?,?,?,?,?)' % self.record_by_car_table_name
        print("execute sql:", sql)
        cursor.execute(sql, record_by_car)
        self.post_ops(conn)

    def query_all_tickets_name(self):
        ops = self.pre_ops()
        conn = ops[0]
        cursor = ops[1]
        sql = 'select ticket_name from %s' % self.ticket_table_name
        print("execute sql:", sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results, type(results))
        self.post_ops(conn)
        return results

    def query_all_coal_names(self):
        ops = self.pre_ops()
        conn = ops[0]
        cursor = ops[1]
        sql = 'select coal_name from %s' % self.coal_table_name
        print("execute sql:", sql)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
        except:
            print("query info from sql failed")
            results = []
        print(results, type(results))
        self.post_ops(conn)
        return results

    def pre_ops(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        return (conn, cursor)

    def post_ops(self, conn):
        conn.commit()
        conn.close()


if __name__ == '__main__':
    sqlUtils = SqlUtils()
    # sqlUtils.delete_table('record_by_car_detail')
    # sqlUtils.add_record_by_car_detail('2017/08/05', 'fff', 'fff', '面煤', '2.00', '北线')
    sqlUtils.query_all_tickets_name()
    # date = time.strftime('%Y/%m/%d', time.localtime(time.time()))  # 当前时间
    # print(date, type(date))
    # sqlUtils.delete_table('tickets')
