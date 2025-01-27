import pymysql

def delete_table ():
    db = pymysql.connect(host='10.12.250.2', user='root', passwd='Dslr*2025!@#', db='my_db', port=3306, charset='utf8')

    cursor = db.cursor()

    cursor.execute("SELECT count(*) FROM city")
    result = str(cursor.fetchone())[1]
    if int(result) == 0:
        print("该表没有数据，正在执行数据插入")
    else:
        print("该表存在数据，正在执行数据清除")

        sql1 = f"""delete from city;"""
        cursor.execute(sql1)
        print("数据清除完成，正在执行数据插入")

    db.commit()
    cursor.close()
    db.close()

if __name__ == '__main__':
    delete_table()
