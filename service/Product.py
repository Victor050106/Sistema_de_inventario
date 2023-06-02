from models.Product import Product as ProductModel
from schemas.Product import Product

class ProductService():
    def __init__(self, db) -> None:
        self.db = db

    def get_product(self):
        result = self.db.query(ProductModel).all()
        return result
        
    def create_product(self,product:ProductModel):
        new_product = ProductModel(
            product_name = product.product_name.upper(),
            product_brand = product.product_brand.upper(),
            product_description = product.product_description.upper(),
            product_price = product.product_price.upper(),
            product_entry_date = product.product_entry_date.upper()
        )
        self.db.add(new_product)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result
    
    def update_product(self,data:Product):
        product = self.db.query(ProductModel).filter(ProductModel.id == data.id).first()
        product.product_name = data.product_name
        product.product_brand = data.product_brand
        product.product_description = data.product_description
        product.product_price = data.product_price
        product.product_entry_date = data.product_entry_date
        self.db.commit()
        return

    def delete_product(self,id:int):
        self.db.query(ProductModel).filter(ProductModel.id == id).delete()
        self.db.commit()
        return