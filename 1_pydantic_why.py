

def insert_patient_data(name:str,age:int): #type hinting 

# Injecting into database just example 
# Type validation is not happening as age is str not num
# Variable value validation is write boilerplate code
    print(name)
    print(age)
    print('inserted into database')

insert_patient_data("nitish",'two5')


# Second Version

def insert_patient_data2(name:str,age:int):

    if type(name) == str and type(age)==int:
        if age<0:
            raise ValueError("Age cannot be Negative")
        else:
            print(name)
            print(age)
            print('inserted into database')
    else:
        raise TypeError("Enter Corrected Datatype value")
    
insert_patient_data2("nitish",-1) 