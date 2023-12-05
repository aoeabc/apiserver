import pymysql
from utils.data_read import data_read
from utils.log_util import logger


class MysqlDb:
    def __init__(self):
        self.host=data_read.data_ini()["mysql"]["mysql_host"]
        self.port=data_read.data_ini()["mysql"]["mysql_port"]
        self.user=data_read.data_ini()["mysql"]["mysql_user"]
        self.password=data_read.data_ini()["mysql"]["mysql_password"]
        self.database=data_read.data_ini()["mysql"]["mysql_db"]
        self.conn=pymysql.connect(host=self.host,
                                  database=self.database,
                                  port=int(self.port),
                                  user=self.user,
                                  password=self.password,
                                  charset="utf8",
                                  autocommit=True)
        self.cursor = self.conn.cursor()


    def find_one(self,sql):
        logger.info("执行sql语句：{}".format(sql))
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        logger.info("sql语句执行结果：{}".format(data))
        return data

    def find_data(self,sql):
        logger.info("执行sql语句：{}".format(sql))
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        logger.info("sql语句执行结果：{}".format(data))
        return data

    def delete_data(self,sql):
        logger.info("执行sql语句：{}".format(sql))
        self.cursor.execute(sql)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

db=MysqlDb()

if __name__ == '__main__':
    db=MysqlDb()
    # data=db.find_one("select * from users_userprofile where mobile ='13488010001' ")
    data=db.find_one("select code from users_verifycode where mobile ='13488010001' order by id desc")
    print(data)
    # db.delete_data("delete from users_verifycode where mobile ='13488010001'")
    # data = db.find_one("select code from users_verifycode where mobile ='13488010001' order by id desc")
    # print(data)
    # tables=(('goods_banner',), ('goods_goods',), ('goods_goodscategory',), ('goods_goodscategorybrand',), ('goods_goodsimage',), ('goods_hotsearchwords',), ('goods_indexad',), ('trade_ordergoods',), ('trade_orderinfo',), ('trade_shoppingcart',), ('user_operation_useraddress',), ('user_operation_userfav',), ('user_operation_userleavingmessage',), ('users_userprofile',), ('users_userprofile_groups',), ('users_userprofile_user_permissions',), ('users_verifycode',))
    # SHOW COLUMNS from users_verifycode



