import pymysql

dbInfo = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'test'
}

sqls = ['select 1', 'select VERSION()']

result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls ):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )

        # 游標建立的時候就開啟了一個隱形的事務
        cur = conn.cursor()
        print(cur)
        try:
            for command in sqls:
                cur.execute(command)
                result.append(cur.fetchone())
                
            #關閉游標
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        conn.close()

if __name__ == "__main__":
    db = ConnDB(dbInfo=dbInfo, sqls=sqls)
    db.run()
    print(result);