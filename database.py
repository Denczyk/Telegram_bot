import pymysql
from bot import *
import re
from datetime import datetime

class find_time():
    def __init__(self, DATABASE):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                port=3306,
                password=password,
                db=db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            print('connect')


        except Exception as ex:
            print('failed')
            print(ex)


        def give_time(self):
            async def messs(message: types.Message):
                await bot.send_message(message.chat.id, 'see')


class add_new_user():
    def __init__(self, DATABASE):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            port=3306,
            password=password,
            db=db_name,
            charset='utf8mb4',
        )


    def start_user(self, id_user):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            port=3306,
            password=password,
            db=db_name,
            charset='utf8mb4',
        )

        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "SELECT id FROM `users`"
                cursor.execute(sql, ())

                for i in cursor.fetchall():
                    print('pl')
                    if id_user == i:
                        break

                    else:
                        with self.connection.cursor() as cursor:
                            sql = "INSERT INTO `users` (id) VALUES (%s)"
                            cursor.execute(sql, (id_user))
                            self.connection.commit()


    def find_user(self, id_user):
        with self.connection:
            user_find = self.cursor.execute('''SELECT * FROM users''').fetchall()

    def add_user(self, id_user, message):
        with self.connection:
            try:
                return self.cursor.execute('''INSERT INTO users (id, rememb) VALUES(?, ?)''', (id_user, message,))

            except:
                return self.cursor.execute(f'''UPDATE users SET rememb = '{message}' WHERE id = '{id_user}' ''')

            finally:
                print('dsplcsd')


class add_plan_to_db():
    def __init__(self, DATABASE):
        try:
            self.connection = pymysql.connect(
            host=host,
            user=user,
            port=3306,
            password=password,
            db=db_name,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
        except:
            print('error1')


    def add_monday(self, data_para, id_user):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                port=3306,
                password=password,
                db=db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
            return self.cursor.execute(f'''UPDATE users SET Monday = '{data_para}' WHERE id = '{id_user}' ''')
        except:
            print('error2')


    def add_tuesday(self, data_para, id_user):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                port=3306,
                password=password,
                db=db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
            return self.cursor.execute(f'''UPDATE users SET Tuesday = '{data_para}' WHERE id = '{id_user}' ''')
        except:
            print('error2.1')


    def add_wednesday(self, data_para, id_user):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                port=3306,
                password=password,
                db=db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
            return self.cursor.execute(f'''UPDATE users SET Wednesday = '{data_para}' WHERE id = '{id_user}' ''')
        except:
            print('error4')


    def add_thursday(self, data_para, id_user):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                port=3306,
                password=password,
                db=db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
            return self.cursor.execute(f'''UPDATE users SET Thursday = '{data_para}' WHERE id = '{id_user}' ''')
        except:
            print('error2')

    def add_friday(self, data_para, id_user):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                port=3306,
                password=password,
                db=db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
            return self.cursor.execute(f'''UPDATE users SET Friday = '{data_para}' WHERE id = '{id_user}' ''')
        except:
            print('error2')

    def add_saturday(self, data_para, id_user):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                port=3306,
                password=password,
                db=db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
            return self.cursor.execute(f'''UPDATE users SET Saturday = '{data_para}' WHERE id = '{id_user}' ''')
        except:
            print('error2')

    def add_sunday(self, data_para, id_user):
        try:
            self.connection = pymysql.connect(
                host=host,
                user=user,
                port=3306,
                password=password,
                db=db_name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connection.cursor()
            return self.cursor.execute(f'''UPDATE users SET Sunday = '{data_para}' WHERE id = '{id_user}' ''')
        finally:
            self.connection.close()


class data_base():
    def __init__(self, DATABASE):
        pass

    async def find_Monday(self, message: types.Message):
        with self.connection:
            content_list = self.cursor.execute('''SELECT Monday FROM users''').fetchall()
            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([[]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '\n', str(content_list))
            await bot.send_message(message.chat.id, "🇺🇦▫Понеділок:🇺🇦 " + content_list)

    async def find_Tuesday(self, message: types.Message):
        with self.connection:
            content_list = self.cursor.execute('''SELECT Tuesday FROM users''').fetchall()
            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([[]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '\n', str(content_list))
            await bot.send_message(message.chat.id, "🇺🇦▫Вівторок:🇺🇦 " + content_list)

    async def find_Wednesday(self, message: types.Message):
        with self.connection:
            content_list = self.cursor.execute('''SELECT Wednesday FROM users''').fetchall()
            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([[]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '\n', str(content_list))
            await bot.send_message(message.chat.id, "🇺🇦▫Середа:🇺🇦 " + content_list)

    async def find_Thursday(self, message: types.Message):
        with self.connection:
            content_list = self.cursor.execute('''SELECT Thursday FROM users''').fetchall()
            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([[]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '\n', str(content_list))
            await bot.send_message(message.chat.id, "🇺🇦▫Четвер:🇺🇦 " + content_list)

    async def find_Friday(self, message: types.Message):
        with self.connection:
            content_list = self.cursor.execute('''SELECT Friday FROM users''').fetchall()
            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([[]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '\n', str(content_list))
            await bot.send_message(message.chat.id, "🇺🇦▫П'ятниця:🇺🇦 " + content_list)


    async def find_Saturday(self, message: types.Message):
        with self.connection:
            content_list = self.cursor.execute('''SELECT Saturday FROM users''').fetchall()
            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([[]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '\n', str(content_list))
            await bot.send_message(message.chat.id, "🇺🇦▫Субота:🇺🇦 " + content_list)


    async def find_Sunday(self, message: types.Message):
        with self.connection:
            content_list = self.cursor.execute('''SELECT Sunday FROM users''').fetchall()
            content_list = re.sub(r'([()]*)', '', str(content_list))
            content_list = re.sub(r'([]]*)', '', str(content_list))
            content_list = re.sub(r'([[]*)', '', str(content_list))
            content_list = re.sub(r"([']*)", "", str(content_list))
            content_list = re.sub(r'([;])', '\n', str(content_list))
            await bot.send_message(message.chat.id, "🇺🇦▫Неділя:🇺🇦 " + content_list)

tm = datetime.now()
print(tm)
