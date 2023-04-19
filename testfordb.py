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

p = 0
f = 0
c = 0
calor = 0
idMeal = 1
test = cursor.execute(f"SELECT IdProduct FROM MEALS_STRUCTURE WHERE IdMeal='{idMeal}'")
test_f = test.fetchall()

def func(cal, naimenovanie):
    for i in test_f:
        print('Айди продукта: ', i[0])
        test2 = cursor.execute(f"SELECT {naimenovanie} FROM PRODUCTS WHERE _idProduct='{i[0]}'")
        test2_f = test2.fetchall()
        test3 = cursor.execute(f"SELECT CountOfProduct FROM MEALS_STRUCTURE WHERE IdMeal='{idMeal}' AND IdProduct='{i[0]}'")
        test3_f = test3.fetchall()
        for j in test2_f:
            for j1 in test3_f:
                print(j[0], j1[0])
                cal += j[0]*j1[0]/100
                print('Сумма: ', round(cal, 1))
    return cal
cursor.execute(f"INSERT INTO MEALS_MAIN (NameMeal, DescriptionMeal, IdGroupMeal, Proteins, Fats, Carbo, Calories) VALUES('test', 'test',  '1'), '{func(p, 'Proteins')}', '{func(f, 'Fats')}', '{func(c, 'Carbo')}', '{func(calor, 'Calories')}'")