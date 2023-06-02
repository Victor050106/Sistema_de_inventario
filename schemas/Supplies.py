from typing import Optional
from pydantic import BaseModel, Field


class Supplies(BaseModel):
    """create Supplies schemas"""
    id: Optional[int] = None
    supplier_id: Optional[int] = None
    product_id: Optional[int] = None
    purchase_price: float = Field(gt=0, description="purchase price")
    
    class Config:
        """example of supplies"""
        schema_extra = {
            "example":{
                "id" : 1,
                "supplier_id" : 1,
                "product_id" : 1,
                "purchase_price" : 9.000
            }
        }