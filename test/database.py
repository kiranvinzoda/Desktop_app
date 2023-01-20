import pymysql.cursors


def create_connection():
    # Connect to the database
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="kiran",
        password="kiran",
        database="pro1",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection