from gettext import Catalog
from itertools import product
from turtle import title
from models import Category
import database as _db, models as _models, schemas as _schemas
import sqlalchemy.orm as _orm


def create_database():
    return _db.Base.metadata.create_all(bind=_db.engine)


def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_category(db: _orm.Session, category: _schemas.CategoryCreate):
    db_category = _models.Category(parent_id=category.parent_id, level=category.level, title=category.title, title_fa=category.title_fa,
    description=category.description, description_fa=category.description_fa, link=category.link, image_link=category.image_link, 
    category = category.category, category_fa = category.category_fa, products = category.products)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db: _orm.Session, id: int = 0, skip: int = 0, limit: int = 1000):
    if id == 0:
        return db.query(_models.Category).offset(skip).limit(limit).all()
        # return db.query(_models.Category).all()
    return db.query(_models.Category).get({"id": id})



def create_product(db: _orm.Session, product: _schemas.ProductCreate, cat_id: int):
    db_product = _models.Product(**product.dict(), category_id = cat_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: _orm.Session, id: int = 0, skip: int = 0, limit: int = 1000):
    if id == 0:
        return db.query(_models.Product).offset(skip).limit(limit).all()
        # return db.query(_models.Product).all()
    return db.query(_models.Product).get({"id": id})

def create_details(db: _orm.Session, detail: _schemas.DetailsCreate, p_id: int):
    db_detail = _models.Details(**detail.dict(), product_id = p_id)
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

def get_details(db: _orm.Session, id: int = 0, product_id: int = 0, skip: int = 0, limit: int = 1000):
    if id == 0:
        if product_id == 0:
            return db.query(_models.Details).offset(skip).limit(limit).all()
        return db.query(_models.Details).get({"product_id": product_id})
        # return db.query(_models.Details).all()
    return db.query(_models.Details).get({"id": id, "product_id": product_id})


def delete_record(db: _orm.Session,  id: int = 0, table_name: str ="all"):
    if table_name == "all":
        db.query(_models.Category).delete()
        db.query(_models.Product).delete()
        db.query(_models.Details).delete()

    elif table_name == "category":
        if id == 0:
            db.query(_models.Category).delete()
        else:
            db.query(_models.Category).filter(_models.Category.id == id).delete()
    
    elif table_name == "product":
        if id == 0:
            db.query(_models.Product).delete()
        else:
            db.query(_models.Product).filter(_models.Category.id == id).delete()

    elif table_name == "details":
        if id == 0:
            db.query(_models.Product).delete()
        else:
            db.query(_models.Product).filter(_models.Category.id == id).delete()
        
    db.commit()