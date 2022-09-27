import MySQLdb

"""
MySQL生成工具类
"""
class sqlCreate():
    def createSql(self):
        return MySQLdb.connect(host='localhost', user='root', password='991010', db='test')