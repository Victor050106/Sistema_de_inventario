from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    """create product schemas"""
    id: Optional[int] = None
    name: str = Field(max_length=30, min_length=1, description="Name of product")
    brand: str = Field(max_length=30, min_length=1, description="Name of brand")
    description: str = Field(max_length=200, min_length=10, description="Description of product")
    price: float = Field(gt=0, description="Price of product")
    entry_date: int = Field(description="entry date")
    