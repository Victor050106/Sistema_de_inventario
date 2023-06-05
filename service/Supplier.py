"""Schemas and models are called"""
from models.Supplier import Supplier as SupplierModel
from schemas.Supplier import Supplier

class SupplierService():
    """Creating the class SupplierService"""
    def __init__(self, db) -> None:
        self.db = db
        
        
    def get_supplier(self):
        result = self.db.query(SupplierModel).all()
        return result
    
    def create_supplier(self,supplier:SupplierModel):
        new_supplier = SupplierModel(
            supplier_name = supplier.supplier_name.upper(),
            supplier_address = supplier.supplier_address.upper(),
            supplier_phone = supplier.supplier_phone.upper(),
            supplier_email = supplier.supplier_email.upper()
        )
        
        self.db.add(new_supplier)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(SupplierModel).filter(SupplierModel.id == id).first()
        return result
    
    def update_supplier(self,data:Supplier):
        supplier = self.db.query(SupplierModel).filter(SupplierModel.id == data.id).first()        
        supplier.supplier_name = data.supplier_name
        supplier.supplier_address = data.supplier_address
        supplier.supplier_phone = data.supplier_phone
        supplier.supplier_email = data.supplier_email
        self.db.commit()
        return
    
    def delete_supplier(self,id:int):
        self.db.query(SupplierModel).filter(SupplierModel.id == id).delete()
        self.db.commit()
        return