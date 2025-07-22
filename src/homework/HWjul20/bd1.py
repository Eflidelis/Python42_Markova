# import psycopg2 as PyPG

# connectBD = PyPG.connect(
#    dbname="Programmers",
#   user="postgres",
#    password="123",
#    host="localhost",
#    port=5432
#)

#cursor = connectBD.cursor()

#query = (
#    "SELECT "
#    "castomers.name AS заказчик, "
#    "projects.title AS проект, "
#    "project_managers.name AS проект_менеджер, "
#    "tasks.description AS задача, "
#    "programmers.name AS ответственный_за_задачу, "
#    "programmers.telephone AS телефон_программиста "
#    "FROM "
#    "castomers "
#    "JOIN projects ON castomers.id = projects.castomer_id "
#    "JOIN project_managers ON projects.id = project_managers.project_id "
#    "JOIN tasks ON projects.id = tasks.project_id "
#    "JOIN team ON tasks.id = team.task_id "
#    "JOIN programmers ON team.programmer_id = programmers.id;"
# )

# cursor.execute(query)

# table = cursor.fetchall()
# for line in table:
#    print(f"{line[0]} - {line[1]} - {line[2]} - {line[3]} - {line[4]} - {line[5]}")

# cursor.close()
# connectBD.close()

import psycopg2

DB_NAME = "Programmers"
DB_USER = "postgres"
DB_PASSWORD = "123"
DB_HOST = "localhost"
DB_PORT = "5432"


def connect_db():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )


def close_db(conn):
    conn.close()


def project_menu(conn):
    while True:
        print("\n1. Создать новый проект")
        print("2. Удалить существующий проект")
        print("3. Изменить данные проекта")
        print("4. Вывести информацию о проекте")
        print("0. Вернуться в главное меню")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_project(conn)
        elif choice == '2':
            delete_project(conn)
        elif choice == '3':
            update_project(conn)
        elif choice == '4':
            get_project_info(conn)
        elif choice == '0':
            break
        else:
            print("Некорректный выбор, введите цифру от 0 до 4")


def create_project(conn):
    title = input("Введите название проекта: ")
    start_date = input("Введите дату начала: ")
    end_date = input("Введите дату окончания: ")
    castomer_id = input("Введите ID заказчика: ")

    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO projects (castomer_id, start_date, end_date, title) VALUES (%s, %s, %s, %s)",
            (castomer_id, start_date, end_date, title)
        )
    conn.commit()
    print("Проект создан")


def delete_project(conn):
    title = input("Введите название проекта для удаления: ")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM projects WHERE title = %s", (title,))
    conn.commit()
    print("Проект удален")


def update_project(conn):
    title = input("Введите название проекта для изменения: ")
    new_title = input("Введите новое название проекта: ")
    new_start_date = input("Введите новую дату начала: ")
    new_end_date = input("Введите новую дату окончания: ")

    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE projects SET title = %s, start_date = %s, end_date = %s WHERE title = %s",
            (new_title, new_start_date, new_end_date, title)
        )
    conn.commit()
    print("Данные проекта изменены")


def get_project_info(conn):
    title = input("Введите название проекта для вывода информации: ")
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM projects WHERE title = %s", (title,))
        project = cursor.fetchone()
        if project:
            print("Информация о проекте:")
            print(f"ID: {project[0]}")
            print(f"ID заказчика: {project[1]}")
            print(f"Дата начала: {project[2]}")
            print(f"Дата окончания: {project[3]}")
            print(f"Название: {project[4]}")
        else:
            print("Такой проект не найден")


def project_manager_menu(conn):
    while True:
        print("\n1. Создать нового проект-менеджера")
        print("2. Удалить существующего проект-менеджера")
        print("3. Изменить данные проект-менеджера")
        print("4. Вывести информацию о проект-менеджере")
        print("0. Вернуться в главное меню")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_project_manager(conn)
        elif choice == '2':
            delete_project_manager(conn)
        elif choice == '3':
            update_project_manager(conn)
        elif choice == '4':
            get_project_manager_info(conn)
        elif choice == '0':
            break
        else:
            print("Некорректный выбор, введите цифру от 0 до 4")


def create_project_manager(conn):
    name = input("Введите имя проект-менеджера: ")
    birthday = input("Введите дату рождения: ")
    telephone = input("Введите телефон: ")
    project_id = input("Введите ID проекта: ")

    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO project_managers (name, birthday, telephone, project_id) VALUES (%s, %s, %s, %s)",
            (name, birthday, telephone, project_id)
        )
    conn.commit()
    print("Проект-менеджер создан")


def delete_project_manager(conn):
    name = input("Введите имя проект-менеджера для отстранения: ")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM project_managers WHERE name = %s", (name,))
    conn.commit()
    print("Проект-менеджер отстранен от работы с проектом")


def update_project_manager(conn):
    name = input("Введите имя проект-менеджера для изменения: ")
    new_name = input("Введите новое имя проект-менеджера: ")
    new_birthday = input("Введите новую дату рождения: ")
    new_telephone = input("Введите новый телефон: ")

    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE project_managers SET name = %s, birthday = %s, telephone = %s WHERE name = %s",
            (new_name, new_birthday, new_telephone, name)
        )
    conn.commit()
    print("Данные проект-менеджера изменены")


def get_project_manager_info(conn):
    name = input("Введите имя проект-менеджера для вывода информации: ")
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM project_managers WHERE name = %s", (name,))
        manager = cursor.fetchone()
        if manager:
            print("Информация о проект-менеджере:")
            print(f"ID: {manager[0]}")
            print(f"Имя: {manager[1]}")
            print(f"Дата рождения: {manager[2]}")
            print(f"Телефон: {manager[3]}")
            print(f"ID проекта: {manager[4]}")
        else:
            print("Такой проект-менеджер не найден")


def task_menu(conn):
    while True:
        print("\n1. Создать новую задачу")
        print("2. Удалить существующую задачу")
        print("3. Изменить данные задачи")
        print("4. Вывести информацию о задаче")
        print("0. Вернуться в главное меню")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_task(conn)
        elif choice == '2':
            delete_task(conn)
        elif choice == '3':
            update_task(conn)
        elif choice == '4':
            get_task_info(conn)
        elif choice == '0':
            break
        else:
            print("Некорректный выбор, введите цифру от 0 до 4")


def create_task(conn):
    description = input("Введите описание задачи: ")
    start_date = input("Введите дату начала: ")
    end_date = input("Введите дату окончания: ")
    project_id = input("Введите ID проекта: ")

    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO tasks (project_id, description, start_date, end_date) VALUES (%s, %s, %s, %s)",
            (project_id, description, start_date, end_date)
        )
    conn.commit()
    print("Новая задача создана")


def delete_task(conn):
    description = input("Введите описание задачи для удаления: ")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM tasks WHERE description = %s", (description,))
    conn.commit()
    print("Задача удалена")


def update_task(conn):
    description = input("Введите описание задачи для изменения: ")
    new_description = input("Введите новое описание задачи: ")
    new_start_date = input("Введите новую дату начала: ")
    new_end_date = input("Введите новую дату окончания: ")

    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE tasks SET description = %s, start_date = %s, end_date = %s WHERE description = %s",
            (new_description, new_start_date, new_end_date, description)
        )
    conn.commit()
    print("Данные задачи изменены")


def get_task_info(conn):
    description = input("Введите описание задачи для вывода информации: ")
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM tasks WHERE description = %s", (description,))
        task = cursor.fetchone()
        if task:
            print("Информация о задаче:")
            print(f"ID: {task[0]}")
            print(f"ID проекта: {task[1]}")
            print(f"Описание: {task[2]}")
            print(f"Дата начала: {task[3]}")
            print(f"Дата окончания: {task[4]}")
        else:
            print("Такая задача не найдена")


def programmer_menu(conn):
    while True:
        print("\n1. Создать нового программиста")
        print("2. Удалить существующего программиста")
        print("3. Изменить данные программиста")
        print("4. Вывести информацию о программисте")
        print("0. Вернуться в главное меню")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_programmer(conn)
        elif choice == '2':
            delete_programmer(conn)
        elif choice == '3':
            update_programmer(conn)
        elif choice == '4':
            get_programmer_info(conn)
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


def create_programmer(conn):
    name = input("Введите имя программиста: ")
    birthday = input("Введите дату рождения: ")
    level = input("Введите уровень (джун, мидл, сеньор): ")
    telephone = input("Введите телефон: ")

    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO programmers (name, birthday, level, telephone) VALUES (%s, %s, %s, %s)",
            (name, birthday, level, telephone)
        )
    conn.commit()
    print("Новый программист нанят")


def delete_programmer(conn):
    name = input("Введите имя программиста для увольнения: ")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM programmers WHERE name = %s", (name,))
    conn.commit()
    print("Программист уволен")


def update_programmer(conn):
    name = input("Введите имя программиста для изменения: ")
    new_name = input("Введите новое имя программиста: ")
    new_birthday = input("Введите новую дату рождения: ")
    new_level = input("Введите новый уровень (джун, мидл, сеньор): ")
    new_telephone = input("Введите новый телефон: ")

    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE programmers SET name = %s, birthday = %s, level = %s, telephone = %s WHERE name = %s",
            (new_name, new_birthday, new_level, new_telephone, name)
        )
    conn.commit()
    print("Данные программиста изменены")


def get_programmer_info(conn):
    name = input("Введите имя программиста для вывода информации: ")
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM programmers WHERE name = %s", (name,))
        programmer = cursor.fetchone()
        if programmer:
            print("Информация о программисте:")
            print(f"ID: {programmer[0]}")
            print(f"Имя: {programmer[1]}")
            print(f"Дата рождения: {programmer[2]}")
            print(f"Уровень: {programmer[3]}")
            print(f"Телефон: {programmer[4]}")
        else:
            print("Такой программист не найден")


def customer_menu(conn):
    while True:
        print("\n1. Создать нового заказчика")
        print("2. Удалить существующего заказчика")
        print("3. Изменить данные заказчика")
        print("4. Вывести информацию о заказчике")
        print("0. Вернуться в главное меню")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_customer(conn)
        elif choice == '2':
            delete_customer(conn)
        elif choice == '3':
            update_customer(conn)
        elif choice == '4':
            get_customer_info(conn)
        elif choice == '0':
            break
        else:
            print("Некорректный выбор, введите цифру от 0 до 4")


def create_customer(conn):
    name = input("Введите имя заказчика: ")
    contact = input("Введите контактное лицо: ")
    telephone = input("Введите телефон: ")

    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO castomers (name, contact, telephone) VALUES (%s, %s, %s)",
            (name, contact, telephone)
        )
    conn.commit()
    print("Заказчик создан")


def delete_customer(conn):
    name = input("Введите имя заказчика для удаления: ")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM castomers WHERE name = %s", (name,))
    conn.commit()
    print("Заказчик удален")


def update_customer(conn):
    name = input("Введите имя заказчика для изменения: ")
    new_name = input("Введите новое имя заказчика: ")
    new_contact = input("Введите новое контактное лицо: ")
    new_telephone = input("Введите новый телефон: ")

    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE castomers SET name = %s, contact = %s, telephone = %s WHERE name = %s",
            (new_name, new_contact, new_telephone, name)
        )
    conn.commit()
    print("Данные заказчика изменены")


def get_customer_info(conn):
    name = input("Введите имя заказчика для вывода информации: ")
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM castomers WHERE name = %s", (name,))
        customer = cursor.fetchone()
        if customer:
            print("Информация о заказчике:")
            print(f"ID: {customer[0]}")
            print(f"Имя: {customer[1]}")
            print(f"Контактное лицо: {customer[2]}")
            print(f"Телефон: {customer[3]}")
        else:
            print("Такой заказчик не найден")


def summary_table(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT 
                castomers.name AS заказчик,
                projects.title AS проект,
                project_managers.name AS проект_менеджер,
                tasks.description AS задача,
                programmers.name AS ответственный_за_задачу,
                programmers.telephone AS телефон_программиста
            FROM 
                castomers 
            JOIN 
                projects ON castomers.id = projects.castomer_id 
            JOIN 
                project_managers ON projects.id = project_managers.project_id 
            JOIN 
                tasks ON projects.id = tasks.project_id 
            JOIN 
                team ON tasks.id = team.task_id 
            JOIN 
                programmers ON team.programmer_id = programmers.id;
        """)
        results = cursor.fetchall()
        print("\nСводная таблица:")
        print(f"{'Заказчик':<30} {'Проект':<40} {'Проект-менеджер':<30} {'Задача':<30} {'Ответственный':<30} {'Телефон':<15}")
        print("=" * 150)
        for row in results:
            print(f"{row[0]:<30} {row[1]:<40} {row[2]:<30} {row[3]:<30} {row[4]:<30} {row[5]:<15}")


def main_menu():
    conn = connect_db()
    try:
        while True:
            print("\n1. Работа с проектами")
            print("2. Работа с проект-менеджерами")
            print("3. Работа с задачами")
            print("4. Работа с программистами")
            print("5. Работа с заказчиками")
            print("6. Вывести сводную таблицу")
            print("0. Выйти")

            choice = input("Выберите действие: ")

            if choice == '1':
                project_menu(conn)
            elif choice == '2':
                project_manager_menu(conn)
            elif choice == '3':
                task_menu(conn)
            elif choice == '4':
                programmer_menu(conn)
            elif choice == '5':
                customer_menu(conn)
            elif choice == '6':
                summary_table(conn)
            elif choice == '0':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
    finally:
        close_db(conn)


if __name__ == "__main__":
    main_menu()


