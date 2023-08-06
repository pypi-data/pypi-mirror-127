Mysql-Tool

= = = = = = = = = =
Install:

    pip install Mysql-Tool
    
Demo:

    from mysql_tool import my_mysql
    host = "******"
    password = "******"
    db = my_mysql(host=host, user="root", port=3306, database="***", password=password)
    
    sql = "select * from aaaa where bbb=%s;"
    data = db.my_fetchone(sql, ['1111'], return_type='dict')
    print(data)


Please use the latest version

1.0.1:

    Encapsulation for pymysql calls


1.0.4:

Solve coding problems
    
    Use from MySQL? Tool.mysql? Tool import my? MySQL


1.0.5:

Use from:
    
        from mysql_tool import my_mysqls

1.0.6: 

    add new function: insert , return id

1.0.7: 

    Add connection pool
    
1.0.9: 

    Add unix_socket 

[View address] (https://github.com/happyshi0402/mysql_tool)!