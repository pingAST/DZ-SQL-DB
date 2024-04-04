from manager_sql import ClientManager

# Пример использования
client_manager = ClientManager(dbname="pyDB", user="postgres", password="password")
# 1. Функция, создающая структуру БД (таблицы).+
client_manager.create_table()
# 2. Функция, позволяющая добавить нового клиента.+
client_manager.add_client("John", "Doe", "doe1@example.com", ["123456789"])
client_manager.add_client("Vic", "Dri", "dr-vi@example.com", ["345540943", "456927395"])
# 6. Функция, позволяющая удалить существующего клиента.+
client_manager.delete_client(2)
# 3. Функция, позволяющая добавить телефон для существующего клиента.+
client_manager.add_phone(3, "987654321")
# 5. Функция, позволяющая удалить телефон для существующего клиента.+
client_manager.delete_phone(1, "987654321")

# 7. Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.+
print(client_manager.find_client("John"))

# 4. Функция, позволяющая изменить данные о клиенте.+
client_manager.update_client_data(6, "Jane2",
                                  "f3ale2", "2email@i.eru")

# 8. Функция, позволяющая изменить данные о клиенте.+
client_manager.change_phone(3, "555555555", "987654321")
