#Invalid Email Exception
class InvalidEmailFormat(Exception):
    def __init__(self,msg):
        self.msg=msg
        super().__init__(self,msg)
Email=input("Enter email address:")
if '@' not in Email or '.' not in Email:
    try:
        raise InvalidEmailFormatError("Email address is invalid")
    except InvalidEmailFormatError as e:
        print(e)
else:
    print("Proceed with Registration")