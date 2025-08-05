from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str ="Male"
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state':'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name':'harish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

# temp = patient1.model_dump() # dict gives
# temp_json = patient1.model_dump_json()
temp = patient1.model_dump(include=['name','age']) # dict gives

temp = patient1.model_dump(exclude={'address':['state']})
temp = patient1.model_dump(exclude_unset=True) 
print(temp)
print(type(temp))