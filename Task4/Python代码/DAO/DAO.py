
class BaseDAO:
    def __init__(self, db):
        self.db = db
        self.conn = db.get_connection()
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        """
        执行通用的数据库查询操作
        """
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_one(self, query, params=None):
        """
        执行查询并获取一条记录
        """
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetch_all(self, query, params=None):
        """
        执行查询并获取所有记录
        """
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        """
        关闭数据库连接
        """
        self.cursor.close()
        self.conn.close()
