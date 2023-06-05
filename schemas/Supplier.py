from pydantic import BaseModel, Field

from typing import Optional


class Supplier (BaseModel):
    id : Optional[int]= None
    sub_name : str = Field(max_length=40,min_length=2,description="name supplier")
    address : str = Field(max_length=40,min_length=2,description="fitting room address")
    phone : int = Field(ge=5)
    email : str = Field(max_length=40,min_length=2,description="provider email")
    
    class config:
        schema_extra = {
            "example":{
                "id":1,
                "sub_name":"Distribuidor gerenrico",
                "address":"cualquiera",
                "phone":3158000000,
                "email":"example@gmail.com"            
            }
        }