import sqlite3


class SqlUtils(object):
    def __init__(self):
        self.conn = sqlite3.connect('..\\db\\account.db')
        self.cursor = self.conn.cursor()
        self.ticket_table_name = 'tickets'
        self.coal_table_name = 'coals'
        self.record_by_car_table_name = 'record_by_car_detail'

    def create_ticket_table_if_necessary(self):
        create_table_sql = '''CREATE TABLE if not exists %s
                     (date text, ticket_name text, purchase_price real, 
                     purchase_compute_way text, sell_price real, sell_compute_way)''' \
                           % self.ticket_table_name
        print(create_table_sql)
        self.cursor.execute(create_table_sql)

    def create_coal_table_if_necessary(self):
        create_coal_table_sql = ''

    def create_record_by_car_detail_table_if_necessary(self):
        create_table_sql = 'CREATE TABLE if not exists %s ' \
                           '(date text, person_name text, car_id text, coal_name text, weight_value real,' \
                           'ticket_name text)' % self.record_by_car_table_name
        print(create_table_sql)
        self.cursor.execute(create_table_sql)

    def delete_table(self, table_name):
        sql = 'DROP TABLE ' + table_name
        self.cursor.execute(sql)
        self.tear_down()

    def add_ticket_record(self, add_date, ticket_name, purchase_compute_way, purchase_price,
                          sell_compute_way, sell_price):
        self.create_ticket_table_if_necessary()
        record = (add_date, ticket_name, purchase_price, purchase_compute_way, sell_price, sell_compute_way)
        sql = 'insert into tickets values(?,?,?,?,?,?)'
        self.cursor.execute(sql, record)
        self.tear_down()

    def add_record_by_car_detail(self, date, person_name, car_id, coal_name, weight_value, ticket_name):
        self.create_record_by_car_detail_table_if_necessary()
        record_by_car = (date, person_name, car_id, coal_name, weight_value, ticket_name)
        print("record info is ", record_by_car)
        sql = 'insert into %s values(?,?,?,?,?,?)' % self.record_by_car_table_name
        print(sql)
        self.cursor.execute(sql, record_by_car)
        self.tear_down()

    def query_all_tickets_name(self):
        sql = 'select ticket_name from %s' % self.ticket_table_name
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print(results, type(results))
        self.tear_down()
        return results

    def query_all_coal_names(self):
        sql = 'select ticket_name from %s' % self.ticket_table_name
        print(sql)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print(results, type(results))
        self.tear_down()
        return results


    def tear_down(self):
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    sqlUtils = SqlUtils()
    # sqlUtils.delete_table('record_by_car_detail')
    # sqlUtils.add_record_by_car_detail('2017/08/05', 'fff', 'fff', '面煤', '2.00', '北线')
    sqlUtils.query_all_tickets_name()
    # date = time.strftime('%Y/%m/%d', time.localtime(time.time()))  # 当前时间
    # print(date, type(date))
    # sqlUtils.delete_table('tickets')
