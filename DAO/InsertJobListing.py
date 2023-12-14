from util.DBConnection import dbConnection
def InsertJobListing():
    try:
        conn, stmt = dbConnection.open()
        JobID = int(input("Job ID: "))
        CompanyID = int(input("Company ID: "))
        JobTitle = input("Job Title: ")
        JobDescription=input("Job Description:")
        JobLocation=input("Job Location")
        Salary=input("Salary:")
        JobType=input("Job Type:")
        PostedDate=input("Posted Date:")
        data = [(JobID,CompanyID,JobTitle,JobDescription,JobLocation,Salary,JobType,PostedDate)]
        create_str='''INSERT INTO JobListing(JobID,CompanyID,JobTitle,JobDescription,JobLocation,Salary,JobType,PostedDate)VALUES (%s, %s, %s,%s,%s,%s,%s,%s)'''
        stmt.executemany(create_str,data)
        conn.commit()
        print("Inserted successfully")

    except Exception as e:
        print(e)
    finally:
        if conn:
            dbConnection.close(conn)

#InsertJobListing()