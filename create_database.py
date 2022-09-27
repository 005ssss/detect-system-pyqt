import sys
import MySQLdb

class database:
    def __init__(self):
        self.user = 'root'      # MySQL用户名
        self.password = '991010'  # MySQL密码
        self.database = 'test'  # 数据库名test
    def createUsers(self):
        self.db = MySQLdb.connect(host='localhost', user=self.user, password =self.password, db=self.database)
        self.cur = self.db.cursor()
        self.cur.execute('''drop table if exists users''')
        sql = '''create table users(
                 user_id int(10) AUTO_INCREMENT,
                 user_name varchar(20),
                 name varchar(20),
                 password varchar(20),
                 PRIMARY KEY (`user_id`)
                 )'''
        self.cur.execute(sql)
        sql = '''insert into users values(%s, %s, %s, %s)''' %(1,"'hp'", "'张三'","'123456'")
        self.cur.execute(sql)
        self.db.commit()
        self.db.close()
    def createCheckData(self):
        self.db = MySQLdb.connect(host='localhost', user=self.user, password =self.password, db=self.database)
        self.cur = self.db.cursor()
        self.cur.execute('''drop table if exists check_data''')
        sql = '''create table check_data(
                 check_id int(10) AUTO_INCREMENT,
                 image_address varchar(100),
                 check_result varchar(100),
                 is_prohibited tinyint(1),
                 check_time datetime,
                 boxes varchar(100),
                 PRIMARY KEY (`check_id`)
                 )'''
        self.cur.execute(sql)
        self.db.close()

if __name__ == '__main__':
    db = database()
    db.createUsers()
    # db.createCheckData()