from pydantic import BaseModel, Field
from typing import Optional

class Supplier(BaseModel):
    """create supplier schema"""
    id: Optional[int] = None
    name: str = Field(max_length=30, min_length=1, description="name of supplier")
    address: str = Field(max_length=20, min_length=1, description="address of supplier")
    phone: int = Field(ge=10,description="phone of supplier")
    email: str = Field(max_length=30, min_length=1,description="Email of supplier")