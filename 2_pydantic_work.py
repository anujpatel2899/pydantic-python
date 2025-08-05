from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    # Type validation first step 
    # Data validation second step like EmailStr,AnyUrl
    # Custom Data Validation for own use case

    # name: str =Field(max_length=50)
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient",
            description="Give name of patient in less than 50 character",
            examples=['anuj', 'amit']
        )
    ]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=100)

    # weight:float = Field(gt=0)
    weight: Annotated[float, Field(gt=0, strict=True)]

    # Not evrything we need evry time optional default value giv
    # married:Optional[bool] = False
    married: Annotated[bool, Field(default=None, description="Is patient married or not")]

    # Two level validation list itself and inside str value as well
    allergies: Annotated[
        Optional[List[str]],
        Field(max_length=5, default=None, description="Number of allergies")
    ]
    # allergies:Optional[List[str]]=None # complex data storing list

    contact_details: Dict[str, str]  # dict 


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient)
    print("Inserted")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("updated")


patient_info = {
    "name": "nitish", 
    "email": "abc@aol.com",
    "linkedin_url": "https://www.linkedin.com/anuj",
    "age": 30,
    "weight": 30.5,
    # "married": True,
    # "allergies": ['pollen', 'dust'],
    "contact_details": {'phone': '5891083'}
}

patient1 = Patient(**patient_info)  # keyword argument in function

insert_patient_data(patient1)
# update_patient_data(patient1)
