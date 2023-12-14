#Job Listing
class JobListing:
    def __init__(self,JobID,CompanyID,JobTitle,JobDescription,JobLocation,Salary,JobType,PostedDate):
        self.JobID=JobID
        self.CompanyID=CompanyID
        self.JobTitle=JobTitle
        self.JobDescription=JobDescription
        self.JobLocation=JobLocation
        self.Salary=Salary
        self.JobType=JobType
        self.PostedDate=PostedDate
        print(f'Job ID={self.JobID} \nCompany ID:{self.CompanyID} \nJob Title:{self.JobTitle} \nJob Description:{self.JobDescription} \nJob Location:{self.JobLocation} \nSalary:{self.Salary} \nJob Type:{self.JobType} \nPosted Date:{self.PostedDate}')

Job=JobListing(2,12,"GET","Graduate Engineer Trainee","Mumbai",45000.00,"Full Time","04/12/2022")