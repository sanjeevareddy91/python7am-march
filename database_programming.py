# install the connector..
# pymysql -- connector for making connection between mysql and python..

# pip install pymysql

# import the connector
import pymysql

# make the connection

conn_obj = pymysql.connect(host='localhost',user='root',password="",database='emp_info')

# create a cursor object.

cur_obj = conn_obj.cursor()

# print(cur_obj)

# cur_obj.execute("create database emp_info")

# print(conn_obj)

# cur_obj.execute("create table emp_personal(first_name char(20),last_name char(20),mobile char(10),address char(100));")

# cur_obj.execute("insert into emp_personal(first_name,last_name,mobile,address) values('rajesh','reddy','8373839876','hyderabad');")

# cur_obj.execute("insert into emp_personal(first_name,last_name,mobile,address) values('suresh','reddy','6473847987','bangalore');")
# cur_obj.execute("insert into emp_personal(first_name,last_name,mobile,address) values('venkatesh','rao','7387849823','Chennai');")

# cur_obj.execute("select * from emp_personal")

# fetchone() -- will fetch the starting record..
# fetchall() -- will fetch all the records..

# print(cur_obj.fetchone())

# print(cur_obj.fetchall())


# cur_obj.execute('select * from emp_personal where last_name="reddy" and address="bangalore"')

# print(cur_obj.fetchall())

# cur_obj.execute("update emp_personal set mobile='9484747734' where first_name='rajesh'")


# cur_obj.execute("delete from emp_personal where first_name='rajesh'")

# cur_obj.execute('truncate emp_personal')

# cur_obj.execute('drop table emp_personal')

# cur_obj.execute('drop database emp_info')
# conn_obj.commit()