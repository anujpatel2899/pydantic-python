from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int 
    weight: float 
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]


    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 must have emergency contact")
        return model

patient_info = {'name':'nitish','email': 'abc@hdfc.com','linkedin_url':'http://linkedin.com/1322', 'age': 65, 'weight': 75.3, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '23456743', 'emergency': '23456743'}}

patient1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print(patient)
    print('updated')


insert_patient_data(patient1)