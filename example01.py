"""
example01 -

@IDE:   PyCharm
@Author:石少全
@Date:2022/4/25 11:16 
@Description: ---


"""
import pymysql


def main():
    no = int(input('要编辑的部门编号'))
    loc = input('部门的新地址')
    conn = pymysql.connect(host='182.92.217.5', port=3306,
                           user='root', password='shishaoquan123.A',
                           db='school', charset='utf8')
    try:
        with conn.cursor() as cursor:
            result = cursor.execute('update tb_dept set dloc=%s where dno=%s', (loc,no))
            if result == 1:
                print('添加成功！')
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
        print(conn)

    finally:
        conn.close()


if __name__ == '__main__':
    main()
