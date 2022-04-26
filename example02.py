"""
example02 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/4/26 9:21 
@Description: ---


"""
import pymysql


def main():
    # no = int(input('要编辑的部门编号'))
    # loc = input('部门的新地址')
    conn = pymysql.connect(host='182.92.217.5', port=3306,
                           user='root', password='shishaoquan123.A',
                           db='school', charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            cursor.execute('select dno as no,dname as name,dloc as loc from tb_dept')
            print(cursor.fetchone())
            print(cursor.fetchone())
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
        print(conn)

    finally:
        conn.close()


if __name__ == '__main__':
    main()
