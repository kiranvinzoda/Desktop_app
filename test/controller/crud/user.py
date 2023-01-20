import pymysql.cursors
from database import create_connection
import uuid
import auth

class User():

    def generate_id():
        id = str(uuid.uuid4())
        return id

    def get_all_user():
        connection = create_connection()

        with connection.cursor() as cursor:
            sql = "SELECT * FROM `users`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def get_user_by_email(email):
        connection = create_connection()

        with connection.cursor() as cursor:
            sql = "SELECT `id`, `email` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, (email))
            result = cursor.fetchone()
            return result

    def get_user_by_email_password(email, password):
        connection = create_connection()

        with connection.cursor() as cursor:
            sql = "SELECT `id`, `email`, `password` FROM `users` WHERE `email`=%s and `password`=%s"
            cursor.execute(sql, (email, password))
            result = cursor.fetchone()
            return result

    def create_user(email, password):
        connection = create_connection()

        hash_password = auth.create_hash_passowrd(password)

        with connection.cursor() as cursor:
            sql = "INSERT INTO `users` (`id`, `email`, `password`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (User.generate_id(), email, hash_password))

            result = connection.commit()    
            return result  

    def update_user():
        connection = create_connection()

        with connection.cursor() as cursor:
            sql = "UPDATE `users` SET `email` = %s, `password` = %s WHERE `id` = 2"
            cursor.execute(sql, ('test2','test2'))

            result = connection.commit()    
            return result           

    def delete_user_by_id(id):
        connection = create_connection()

        with connection.cursor() as cursor:
            sql = "DELETE FROM `users` WHERE `email` =%s"
            cursor.execute(sql, (id))

            result = connection.commit()    
            return result        






