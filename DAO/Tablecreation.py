from util.DBConnection import dbConnection
def TableCreation():
    conn=None
    try:
        conn,stmt=dbConnection.open()
        if conn:
            stmt.execute('''create table if not exists Company(CompanyID INT PRIMARY KEY, CompanyName varchar(30),Location varchar(30))''')
            stmt.execute('''create table  if not exists JobListing(JobID INT PRIMARY KEY, CompanyID int,JobTitle varchar(20),JobDescription varchar(100),JobLocation varchar(30),Salary float,JobType varchar(20),PostedDate datetime)''')
            stmt.execute('''create table  if not exists Applicant(ApplicantID INT PRIMARY KEY,FirstName varchar(20),LastName varchar(20),Email varchar(30),Phone char(10),Resume varchar(255))''')
            stmt.execute('''create table if not exists JobApplication(ApplicationID int primary key,JobID int,ApplicantID int,ApplicationDate datetime,coverLetter varchar(100))''')
            print("Database connected.")
    except Exception as e:
        print(e)
    finally:
        if conn:
            dbConnection.close(conn)
TableCreation()