import pymysql
import pymysql.cursors

from pylib.service.log_service import Logger


class MySQL:
    def __init__(self, host:str, port:int, user:str, password:str, db:str) -> None:
        self.conn = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    def find(self, query:str, args:object) -> any:
        try:
            cur = self.conn.cursor()
            cur.execute(query, args)
            result = cur.fetchone()
        finally:
            if cur is not None:
                cur.close()
        return result
    
    def find_all(self, query:str, args:object = None) -> list:
        try:
            cur = self.conn.cursor()
            cur.execute(query, args)
            results = cur.fetchall()
        finally:
            if cur is not None:
                cur.close()
        return results

    def execute(self, query:str, args:object) -> int:
        lastId = 0
        try:
            cur = self.conn.cursor()
            cur.execute(query, args)
            self.conn.commit()
            lastId = cur.lastrowid
        except Exception as e:
            Logger.to().add(e)
        finally:
            if cur is not None:
                cur.close()
        return lastId

    def execute_many(self, query:str, args:object):
        try:
            cur = self.conn.cursor()
            cur.executemany(query, args)
            self.conn.commit()
        except Exception as e:
            pass
        finally:
            if cur is not None:
                cur.close()