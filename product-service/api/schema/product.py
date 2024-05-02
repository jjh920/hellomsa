from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float

    class Config:
        from_attributes=True


class ProductCreate(ProductBase):
    pass

    class Config:
        from_attributes=True


class Product(ProductBase):
    pno: int



