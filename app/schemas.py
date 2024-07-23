import pydantic as _pydantic
import typing as _typing

class _ProductBase(_pydantic.BaseModel):
    title: str
    title_fa: str
    link: str
    image_link: str
    description: str
    description_fa: str 
    digital_catalog: str
    catalogs: str
    details_link: str
    technical_data_pdf: str
    features: str
    features_fa: str
    parent_id: int


class ProductCreate(_ProductBase):
    pass


class Product(ProductCreate):
    id: int
    category_id: int

    # to prevent lazy-loading
    class Config:
        orm_mode = True

        

class _CategorytBase(_pydantic.BaseModel):
    level: int
    title: str
    title_fa: str
    description: str
    description_fa: str 
    link: str
    image_link: str
    category: str
    category_fa: str
    parent_id: int
    products: _typing.List[Product] = []



class CategoryCreate(_CategorytBase):
    pass


class Category(CategoryCreate):
    id: int
    # parent_id: int = id


    # to prevent lazy-loading
    class Config:
        orm_mode = True


class _DetailsBase(_pydantic.BaseModel):
    key: str
    value: str


class DetailsCreate(_DetailsBase):
    pass


class Details(DetailsCreate):
    id: int
    product_id: int

    # to prevent lazy-loading
    class Config:
        orm_mode = True