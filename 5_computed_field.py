from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int 
    weight: float #kg
    height : float #mtr
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    # self.weight refers to the weight of that particular patient.
    # self.height refers to that patient's height.
    # self lets you access the data inside the object from within the method.
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi

patient_info = {'name':'nitish','email': 'abc@hdfc.com', 'age': 65, 'weight': 75.3, 'height': 1.73, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '23456743', 'emergency': '23456743'}}

patient1 = Patient(**patient_info)

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI', patient.bmi)
    print('updated')


insert_patient_data(patient1)