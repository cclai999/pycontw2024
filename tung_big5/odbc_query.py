def fetch_data_from_informix(data_source_name, sql_command, sql_params=tuple()):
    with pyodbc.connect(f"DSN={data_source_name}", autocommit=False) as conn:
        conn.setencoding(encoding='tung_big5')
        conn.setdecoding(pyodbc.SQL_CHAR, encoding='tung_big5')
        conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='utf-32le')
        with conn.cursor() as cursor:
            cursor.execute(sql_command, sql_params)
            records = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
    return [
        dict(zip(columns, row))
        for row in records
    ]