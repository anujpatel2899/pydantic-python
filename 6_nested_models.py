from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'haldwani', 'state':'uttarakhand', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name':'harish', 'gender': 'male', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.state)
print(patient1.address.pin)
print(patient1.address.city)