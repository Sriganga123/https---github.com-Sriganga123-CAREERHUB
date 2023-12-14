from DAO.Tablecreation import TableCreation
from DAO.InsertJobListing import InsertJobListing
from DAO.InsertCompany import InsertCompany
from DAO.InsertJobApplication import InsertJobApplication
from DAO.InsertApplicant import InsertApplicant
from DAO.GetJobListings import GetJobListings
from DAO.GetCompanies import GetCompanies
from DAO.GetJobApplications import GetJobApplications
from DAO.GetApplicants import GetApplicants

if __name__ == '__main__':
    try:
        while True:
            print("1.Insert Job Listing")
            print("2.Insert Company")
            print("3.Insert Job Application")
            print("4.Insert Applicant")
            print("5.Get Job Listings")
            print("6.Get Companies")
            print("7.Get Job Applications")
            print("8.Get Applicants")
            print("9.Exit")
            choice=input("Enter your choice:")
            if choice=='1':
                InsertJobListing()
            elif choice=='2':
                InsertCompany()
            elif choice=='3':
                InsertJobApplication()
            elif choice=='4':
                InsertApplicant()
            elif choice=='5':
                GetJobListings()
            elif choice=='6':
                GetCompanies()
            elif choice=='7':
                GetJobApplications()
            elif choice=='8':
                GetApplicants()
            elif choice=='9':
                break
            else:
                print("Invalid Choice")
    except Exception as e:
        print(e)

