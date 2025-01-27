import pymysql

def insert_db (province, city, area):
    db = pymysql.connect(host='10.12.250.2', user='root', passwd='Dslr*2025!@#', db='my_db', port=3306, charset='utf8')

    cursor = db.cursor()

    sql1 = f"""insert into city(province, city, area) values('{province}', '{city}', '{area}')"""

    cursor.execute(sql1)

    db.commit()
    cursor.close()
    db.close()

if __name__ == '__main__':
    province = input('请输入省份信息:')
    city = input('请输入市区信息:')
    area = input('请输入区域信息:')
    print("数据插入完成")
