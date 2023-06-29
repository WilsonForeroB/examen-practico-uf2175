import mysql.connector


def connection_database(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(3307)
    )

    return connection


def get_users(query, connection):
    results = execute_query(query, connection)
    return results


def execute_query(query, connection):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


if __name__ == '__main__':
    conn = connection_database('127.0.0.1', 'root', 'root', 'gri')
    query = "SELECT nombre FROM users"
    print(get_users(query, conn))



