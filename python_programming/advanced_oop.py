import math
class Contact:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.full_info=first_name+""+last_name
    def print_contact(self):
        print(self.full_info)

class EmailContact(Contact):
    def __init__(self,first_name,last_name,email):
        super().__init__(first_name,last_name)
        self.email=email
        self.full_info=email

email_contact=EmailContact("test","person","nshuti@gmaiol.com")
email_contact.print_contact()
print(math.factorial(4))
from math import pi
print(pi)
