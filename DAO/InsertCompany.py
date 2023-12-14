from util.DBConnection import dbConnection
def InsertCompany():
    try:
        conn, stmt = dbConnection.open()
        CompanyID = int(input("Company ID: "))
        CompanyName = input("Company Name: ")
        Location = input("Location: ")
        data = [(CompanyID,CompanyName,Location)]
        create_str='''INSERT INTO Company(CompanyID, CompanyName, Location)VALUES (%s, %s, %s)'''
        stmt.executemany(create_str, data)
        conn.commit()
        print("Inserted successfully")

    except Exception as e:
        print(e)
    finally:
        if conn:
            dbConnection.close(conn)

#InsertCompany()