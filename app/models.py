import datetime as _dt
from email.policy import default
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import database as _db
from sqlalchemy.dialects.mysql import LONGTEXT as _lt

class Category(_db.Base):
    __tablename__ = "SMC_categories"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    parent_id = _sql.Column(_sql.Integer, _sql.ForeignKey("SMC_categories.id"))
    level = _sql.Column(_sql.Integer, default=0)
    title = _sql.Column(_lt, default="")
    title_fa = _sql.Column(_lt, default="")
    description = _sql.Column(_lt, default="")
    description_fa = _sql.Column(_lt, default="")
    link = _sql.Column(_lt)
    image_link = _sql.Column(_lt)
    category = _sql.Column(_lt)
    category_fa = _sql.Column(_lt)

    child = _orm.relationship("Category")
    products = _orm.relationship("Product", back_populates="category")

class Product(_db.Base):
    __tablename__ = "SMC_products"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    title = _sql.Column(_lt)
    title_fa = _sql.Column(_lt)
    link = _sql.Column(_lt) ############
    image_link = _sql.Column(_lt)
    description = _sql.Column(_lt, default="")
    description_fa = _sql.Column(_lt, default="")
    digital_catalog = _sql.Column(_lt, default="") 
    catalogs = _sql.Column(_lt, default="")
    details_link = _sql.Column(_lt, default="")
    technical_data_pdf = _sql.Column(_lt, default="") ############
    features = _sql.Column(_lt, default="") ############
    features_fa = _sql.Column(_lt, default="") ############
    parent_id = _sql.Column(_sql.Integer, _sql.ForeignKey("SMC_products.id"))

    category_id = _sql.Column(_sql.Integer, _sql.ForeignKey("SMC_categories.id"))
    category = _orm.relationship("Category", back_populates="products")
    child = _orm.relationship("Product")
    details = _orm.relationship("Details", back_populates="product")

class Details(_db.Base): ############
    __tablename__ = "SMC_details_tables"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    product_id = _sql.Column(_sql.Integer, _sql.ForeignKey("SMC_products.id")) #, default = 0)
    key = _sql.Column(_lt)
    value = _sql.Column(_lt)

    product = _orm.relationship("Product", back_populates="details")


