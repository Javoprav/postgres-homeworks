"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os, psycopg2

if __name__ == '__main__':
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='12345'
    )

    cur = conn.cursor()
    customers_data = os.path.join('north_data', 'customers_data.csv')
    employees_data = os.path.join('north_data', 'employees_data.csv')
    orders_data = os.path.join('north_data', 'orders_data.csv')
    f = open(employees_data, 'r')
    cur.copy_from(f, 'employees', sep=',')
    f.close()