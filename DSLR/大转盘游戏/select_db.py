import pymysql

area_lists = []
def select_table ():

    db = pymysql.connect(host='10.12.250.2', user='root', passwd='Dslr*2025!@#', db='my_db', port=3306, charset='utf8')

    cursor = db.cursor()

    cursor.execute("select area from city")
    results = cursor.fetchall()
    for row in range(len(results)):

        area_lists.append(results[row][0])
    return area_lists

    db.commit()
    cursor.close()
    db.close()

if __name__ == '__main__':
    print(select_table())
