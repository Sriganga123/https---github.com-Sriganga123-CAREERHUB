#Company Class
class Company:
    def __init__(self,CompanyID,CompanyName,Location):
        self.CompanyID=CompanyID
        self.CompanyName=CompanyName
        self.Location=Location
        print(f'Company ID:{self.CompanyID} Company Name:{self.CompanyName} Location:{Location}')

c=Company(45,"TCS","Pune")