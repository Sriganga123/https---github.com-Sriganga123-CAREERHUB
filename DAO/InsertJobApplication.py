from util.DBConnection import dbConnection
def InsertJobApplication():
    try:
        conn, stmt = dbConnection.open()
        ApplicationID = int(input("Application ID: "))
        JobID = int(input("Job ID: "))
        ApplicantID = int(input("Applicant ID: "))
        ApplicationDate=input("Application Date")
        coverLetter=input("Cover Letter")
        data = [(ApplicationID,JobID,ApplicantID,ApplicationDate,coverLetter)]
        create_str='''INSERT INTO JobApplication(ApplicationID,JobID,ApplicantID,ApplicationDate,coverLetter)VALUES (%s, %s, %s,%s,%s)'''
        stmt.executemany(create_str,data)
        conn.commit()
        print("Inserted successfully")

    except Exception as e:
        print(e)
    finally:
        if conn:
            dbConnection.close(conn)

#InsertJobApplication()