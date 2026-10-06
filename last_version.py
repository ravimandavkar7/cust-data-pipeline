def get_last_version(conn):
    query="""SELECT LAST_VERSION FROM ETL_WATERMARK WHERE PROCESS_NAME = 'CUSTOMERS'""";

    cursor=conn.cursor()
    cursor.execute(query)

    row=cursor.fetchone()
    return row[0]