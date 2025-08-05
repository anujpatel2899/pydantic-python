from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

# Define a Pydantic model to validate and parse patient data
class Patient(BaseModel):

    # Basic field definitions with type hints
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int 
    weight: float 
    married: bool 
    allergies: List[str]
    contact_details: Dict[str, str]

    # Custom validator for email field
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']  # allowed email domains
        # Example: abc@gmail.com → domain = gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")  # raise error if domain not allowed

        return value  # return value if domain is valid
    
    # Custom validator to transform name field (e.g., make uppercase)
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()  # transform name to uppercase

    # default mode is 'after'
    @field_validator('age', mode='after')  # default type coercion mode: 'after'
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:  # allow only age between 1 and 99
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")  # raise error otherwise

# Before method: dictionary with string/int/float/bool values
patient_info = {
    'name': 'nitish',
    'email': 'abc@hdfc.com',
    'linkedin_url': 'http://linkedin.com/1322',
    'age': '30',  # passed as string to test coercion
    'weight': 75.3,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '23456743'}
}

# After Pydantic: creates a validated Patient object
patient1 = Patient(**patient_info)

# Function to insert patient data
def insert_patient_data(patient: Patient):
    print(patient.name)          # transformed name (uppercase)
    print(patient.age)           # validated and coerced age
    print(patient.allergies)     # list of allergies
    print(patient.married)       # bool field
    print(patient)               # full patient model
    print('updated')

# Call the function with validated patient object
insert_patient_data(patient1)
