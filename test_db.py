import pymysql
import os

host = os.getenv('DB_HOST', 'localhost')
port = int(os.getenv('DB_PORT', 3306))
user = os.getenv('DB_USERNAME', 'root')
password = os.getenv('DB_PASSWORD', '')
database = os.getenv('DB_DATABASE', 'metrostroi')

print(f"Параметры подключения:")
print(f"  Хост: '{host}'")
print(f"  Порт: {port}")
print(f"  База: '{database}'")
print(f"  Юзер: '{user}'")

try:
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        connect_timeout=10
    )
    print("✅ Подключение к БД УСПЕШНО!")
    conn.close()
except Exception as e:
    print(f"❌ Ошибка: {e}")
    print(f"Тип ошибки: {type(e).__name__}")