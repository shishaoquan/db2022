"""
example01 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/4/25 11:16 
@Description: ---


"""
import pymysql


def main():
    # no = int(input('要编辑的部门编号'))
    # loc = input('部门的新地址')
    conn = pymysql.connect(host='182.92.217.5', port=3306,
                           user='root', password='',
                           db='school', charset='utf8')
    try:
        with conn.cursor() as cursor:
            cursor.execute('select dno,dname,dloc from tb_dept')
            for row in cursor.fetchall():
                print(f'部门编号：{row[0]}')
                print(f'部门名称：{row[1]}')
                print(f'部门所在地：{row[2]}')
                print('-'*20)
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
        print(conn)

    finally:
        conn.close()


if __name__ == '__main__':
    main()
