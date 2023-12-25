class BaseDAO:
    def __init__(self, db):
        self.db = db

    def execute_query(self, query, params=None):
        """
        执行通用的数据库查询操作
        """
        try:
            with self.db.get_connection() as conn, conn.cursor() as cursor:
                if params is None:
                    cursor.execute(query)
                else:
                    cursor.execute(query, params)
                conn.commit()
        except Exception as e:
            print(f"执行查询时出错: {e}")

    def fetch_one(self, query, params=None):
        """
        执行查询并获取一条记录
        """
        result = None
        try:
            with self.db.get_connection() as conn, conn.cursor() as cursor:
                if params is None:
                    cursor.execute(query)
                else:
                    cursor.execute(query, params)
                result = cursor.fetchone()
        except Exception as e:
            print(f"获取记录时出错: {e}")
        return result

    def fetch_all(self, query, params=None):
        """
        执行查询并获取所有记录
        """
        results = None
        try:
            with self.db.get_connection() as conn, conn.cursor() as cursor:
                if params is None:
                    cursor.execute(query)
                else:
                    cursor.execute(query, params)
                results = cursor.fetchall()
        except Exception as e:
            print(f"获取所有记录时出错: {e}")
        return results
