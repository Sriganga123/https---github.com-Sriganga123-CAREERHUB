#Applicant Class
class Applicant:
    def __init__(self,ApplicantID,FirstName,LastName,Email,Phone,Resume):
        self.ApplicantID=ApplicantID
        self.FirstName=FirstName
        self.LastName=LastName
        self.Email=Email
        self.Phone=Phone
        self.Resume=Resume
        print(f'Applicant ID:{self.ApplicantID} \nFirst Name:{self.FirstName} \nLast Name:{self.LastName} \nEmail={self.Email} \nPhone={self.Phone} \nResume:{self.Resume}')

a=Applicant(24,"Sriganga","Vuthur","vuthursriganga@gmail.com",'8247238787','Submitted')