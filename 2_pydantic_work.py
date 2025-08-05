from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List,Dict,Optional


class Patient(BaseModel):
    # Type validation first step 
    # Data validation second step like EmailStr,AnyUrl
    name: str
    email: EmailStr
    linkedin_url:AnyUrl
    age: int 
    weight:float
    # Not evrything we need evry time optional default value giv
    married:Optional[bool] = False
    # Two level validation list itself and inside str value as well
    allergies:Optional[List[str]]=None # complex data storing list
    contact_details: Dict[str,str] # dict 

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient)
    print("Inserted")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("updated")

patient_info = {
    "name":"nitish", 
    "email":"abc@aol.com",
    "linkedin_url":"https://www.linkedin.com/anuj",
    "age":30,
    'weight':30.5,
    # "married":True,
    # "allergies":['pollen','dust'],
    "contact_details":{'phone':'5891083'}
    }

patient1 = Patient(**patient_info) # keyword argument in function


insert_patient_data(patient1)
# update_patient_data(patient1)