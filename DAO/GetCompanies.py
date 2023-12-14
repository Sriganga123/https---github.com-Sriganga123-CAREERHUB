from util.DBConnection import dbConnection
def GetCompanies():
        try:
            conn,stmt=dbConnection.open()
            select_str='''select * from Company'''
            stmt.execute(select_str)
            data=stmt.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)
#GetCompanies()

