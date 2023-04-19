from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

try:
    sqlite_connection = sqlite3.connect('C:\sqlite\BeHealthyDatabase.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")


    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    #cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')

    def logger(self):
        self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'
        user = self.root.ids.user.text
        password = self.root.ids.password.text
        cursor.execute(f"INSERT INTO USERS (Name, Password) VALUES ('{user}', '{password}')")
        sqlite_connection.commit()

    def clear(self):
        self.root.ids.welcome_label.text = "WELCOME"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""


MainApp().run()