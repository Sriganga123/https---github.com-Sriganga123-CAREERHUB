#Job Application
class JobApplication:
    def __init__(self,ApplicationID,JobID,ApplicantID,ApplicationDate,coverLetter):
        self.ApplicationID=ApplicationID
        self.JobID=JobID
        self.ApplicantID=ApplicantID
        self.ApplicationDate=ApplicationDate
        self.coverLetter=coverLetter
        print(f'Application ID:{self.ApplicationID} \nJob ID:{self.JobID} \nApplicant ID:{self.ApplicantID} \nApplication Date:{self.ApplicationDate} Cover Letter:{self.coverLetter}')

J=JobApplication(10,1,23,'06/01/2002',"Submitted")