import random

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
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
"""finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")"""

class MainApp(App):
    '''def build(self):
        #hello world
        p = cursor.execute("SELECT Description FROM ACTIVITY ORDER BY IdActivity")
        label = Label(text=f"Выберите образ жизни:",
                      size_hint=(1, 1),
                      pos_hint={'center_x': .5, 'center_y': .8})
        #return label
        #boxlayout
        layout = BoxLayout(padding=20, orientation = 'vertical')
        layout.add_widget(label)
        test=[]
        p_tuple = p.fetchall()
        for i in p_tuple:
            print(i[0])
            test.append(i[0])
        for i in test:
            btn = Button(text=f'{i}')
            layout.add_widget(btn)
        return layout
        #gridlayout
        layout=GridLayout(cols=2, rows=2, row_force_default=True, row_default_height=40)
        colors = ['red', 'green', 'blue', 'purple']
        for i in colors:
            btn = Button(text=f'Кнопка цвета {i}', background_color=i)
            layout.add_widget(btn)
        return layout'''


    #cursor.execute(f"INSERT INTO MEALS_MAIN(Proteins, Fats, Carbo, Calories) VALUES ({p}, {f}, {c}, {cal})")


if __name__=="__main__":
    MainApp().run()