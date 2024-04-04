import psycopg2
import json


class ClientManager:
    def __init__(self, dbname, user, password):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
        )

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            email VARCHAR(50),
            phones VARCHAR[]
        )
        """)
        self.conn.commit()

    def add_client(self, first_name, last_name, email, phones=None):
        cursor = self.conn.cursor()

        # Проверяем, есть ли уже клиент с таким email
        cursor.execute("""
        SELECT id
        FROM clients
        WHERE email = %s
        """, (email,))
        result = cursor.fetchone()
        if result:
            print(f"Клиент с адресом электронной почты {email} уже существует.")
            return

        # Проверяем формат электронной почты
        if "@" not in email or "." not in email:
            print(
                "Неверный формат электронной почты. Электронная почта должна содержать символ @ и хотя бы одну точку.")
            return

        # Если клиент с таким email не найден и email соответствует формату, добавляем нового клиента
        cursor.execute("""
        INSERT INTO clients (first_name, last_name, email, phones)
        VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, email, phones))

        self.conn.commit()
        print(f"Клиент {first_name} {last_name} успешно добавлен с адресом электронной почты {email}")

    def add_phone(self, client_id, phone):
        cursor = self.conn.cursor()

        # Проверяем, есть ли уже такой номер телефона у клиента
        cursor.execute("""
        SELECT phones
        FROM clients
        WHERE id = %s
        """, (client_id,))

        result = cursor.fetchone()
        if result:
            client_phones = result[0]
            if phone in client_phones:
                print(f"Телефон {phone} уже связан с идентификатором клиента {client_id}.")
                return

        # Если номер телефона не найден, добавляем его
        cursor.execute("""
        UPDATE clients
        SET phones = array_append(phones, %s)
        WHERE id = %s
        """, (phone, client_id))

        self.conn.commit()
        print(f"Телефон {phone} успешно добавлен клиенту с идентификатором {client_id}")

    def update_client_data(self, client_id, first_name=None, last_name=None, email=None):
        cursor = self.conn.cursor()
        update_query = "UPDATE clients SET"
        update_params = []

        if first_name:
            update_query += " first_name = %s,"
            update_params.append(first_name)
        if last_name:
            update_query += " last_name = %s,"
            update_params.append(last_name)
        if email:
            # Проверяем формат обновляемой электронной почты
            if "@" not in email or "." not in email:
                print("Неверный формат электронной почты. Электронная почта должна содержать знак «@» и хотя бы одну "
                      "точку")
                return
            update_query += " email = %s,"
            update_params.append(email)

        if not (first_name or last_name or email):
            print("Error: No data to update.")
            return False

        update_query = update_query.rstrip(",") + " WHERE id = %s"
        update_params.append(client_id)

        cursor.execute(update_query, tuple(update_params))
        self.conn.commit()
        print("Данные обновлены")

    def delete_phone(self, client_id, phone):
        cursor = self.conn.cursor()

        # Проверяем, принадлежит ли указанный телефон клиенту с указанным идентификатором
        cursor.execute("""
        SELECT id
        FROM clients
        WHERE id = %s AND %s = ANY(phones)
        """, (client_id, phone))

        result = cursor.fetchone()
        if not result:
            print(f"Телефон {phone} не принадлежит клиенту с идентификатором {client_id}.")
            return

        # Если телефон принадлежит клиенту, удаляем его из списка телефонов клиента
        cursor.execute("""
        UPDATE clients
        SET phones = array_remove(phones, %s)
        WHERE id = %s
        """, (phone, client_id))

        self.conn.commit()
        print(f"Телефон {phone} удален из клиента с идентификатором {client_id}.")

    def delete_client(self, client_id):
        cursor = self.conn.cursor()

        # Проверяем, существует ли клиент с указанным идентификатором
        cursor.execute("""
        SELECT id
        FROM clients
        WHERE id = %s
        """, (client_id,))

        result = cursor.fetchone()
        if not result:
            print(f"Клиент с идентификатором {client_id} не существует.")
            return

        # Если клиент с указанным идентификатором найден, удаляем его из базы данных
        cursor.execute("""
        DELETE FROM clients
        WHERE id = %s
        """, (client_id,))

        self.conn.commit()
        print(f"Клиент с идентификатором {client_id} удален.")

    def find_client(self, search_term):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT * FROM clients
        WHERE first_name = %s OR last_name = %s OR email = %s OR %s = ANY(phones)
        """, (search_term, search_term, search_term, search_term))

        result = cursor.fetchall()

        # Преобразование данных в формат JSON с красивым форматированием
        json_result = []
        for row in result:
            client_data = {
                'id': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'email': row[3],
                'phones': row[4]
            }
            json_result.append(client_data)

        return json.dumps(json_result, indent=4)

    def change_phone(self, client_id, old_phone, new_phone):
        cursor = self.conn.cursor()

        # Проверяем, содержит ли массив телефонов старый номер телефона
        cursor.execute("""
        SELECT id
        FROM clients
        WHERE id = %s AND %s = ANY(phones)
        """, (client_id, old_phone))

        result = cursor.fetchone()
        if not result:
            print(f"У клиента с идентификатором {client_id} нет номера телефона {old_phone}.")
            return

        # Если старый номер телефона найден, обновляем его на новый номер
        cursor.execute("""
        UPDATE clients
        SET phones = array_replace(phones, %s, %s)
        WHERE id = %s
        """, (old_phone, new_phone, client_id))

        self.conn.commit()
        print(f"Номер телефона {old_phone} изменен на {new_phone} для клиента с идентификатором {client_id}")
