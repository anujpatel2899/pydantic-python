from pydantic import BaseModel


class Patient(BaseModel):
    # Type validation first step
    name: str 
    age: int 
    weight:float

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("Inserted")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("updated")

patient_info = {"name":"nitish","age":30,'weight':30.5}

patient1 = Patient(**patient_info) # keyword argument in function


# insert_patient_data(patient1)
update_patient_data(patient1)