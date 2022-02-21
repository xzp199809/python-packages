# coding=utf-8
import pymysql


class Mysql(object):
    def __init__(self, db_name: str, flag: bool):
        self.dbname = db_name
        self.port = 3306
        self.host = '127.0.0.1'
        self.user = 'root'
        self.passwd = '590128xzp.'
        self.charset = 'utf-8'
        self.conn, self.cursor = self.get_conn(flag)

    # def get_conn(self, f: bool):
    #     return self._get_conn(f)

    def get_conn(self, f: bool):
        if f:
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                   passwd=self.passwd, db=self.dbname, charset=self.charset)
            cursor = conn.cursor()
            return conn, cursor
        else:
            return None, None

    def close(self):
        self.cursor.close()
        self.conn.close()

    def check_table(self):
        tables = self.cursor.execute('show tables').fetchall()
        return tables


if __name__ == '__main__':
    m = Mysql(db_name='b_types', flag=True)
    print(m.check_table())