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
    try:
        """sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"      # заполнение работает
        e = open('north_data/employees_data.csv', 'r', encoding='utf8')
        cur.execute("truncate " + 'employees' + ";")
        cur.copy_expert(sql=sql % 'employees', file=e)
        e.close()"""

        f = open(employees_data, 'r', encoding='utf8') # с этим не проходит
        cur.copy_from(f, 'employees', sep=',')
        f.close()

        f = open(customers_data, 'r')        # заполнение работает
        cur.copy_from(f, 'customers', sep=',')
        f.close()

        f = open(orders_data, 'r')           # заполнение работает
        cur.copy_from(f, 'orders', sep=',')
        f.close()

    finally:
        conn.commit()
        cur.close()
        conn.close()