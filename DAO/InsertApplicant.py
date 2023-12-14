from util.DBConnection import dbConnection
def InsertApplicant():
    try:
        conn, stmt = dbConnection.open()
        ApplicantID = int(input("Applicant ID: "))
        FirstName = input("First Name: ")
        LastName = input("Last Name: ")
        Email=input("Email:")
        Phone=input("Phone:")
        Resume=input("Resume")
        data = [(ApplicantID, FirstName, LastName, Email, Phone, Resume)]
        create_str='''INSERT INTO Applicant (ApplicantID, FirstName, LastName, Email, Phone, Resume)VALUES (%s, %s, %s, %s, %s, %s)'''
        stmt.executemany(create_str, data)
        conn.commit()
        print("Inserted successfully")

    except Exception as e:
        print(e)
    finally:
        if conn:
            dbConnection.close(conn)

#InsertApplicant()