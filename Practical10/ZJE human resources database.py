class Staff(object):
    def __init__(self,first_name,last_name,location,role):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.role = role
#Create a class and defind the four attributes

    def staff_information(self):
        print(self.first_name," ",self.last_name,"\t",self.location,"\t",self.role)
#Create a function to print the staff's all information in one line

first_name = input("Your first name is:")
last_name = input("Your last name is:")
location = input("Your location is:")
role = input("Your role is:")
#Input the staff's information

staff1 = Staff(first_name,last_name,location,role)
#Create an instance
staff1.staff_information()
#Apply the function to this instance

#example
staff2 = Staff('Bob','Lewis','Edinburgh','faculty')
staff2.staff_information()

    

