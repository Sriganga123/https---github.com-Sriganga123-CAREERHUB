from util.DBConnection import dbConnection
def GetJobApplications():
        try:
            conn,stmt=dbConnection.open()
            select_str='''select * from JobApplication'''
            stmt.execute(select_str)
            data=stmt.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)
#GetJobApplications()

