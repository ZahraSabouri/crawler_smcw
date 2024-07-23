from re import U
import fastapi as _fastapi
from sqlalchemy import orm as _orm
import typing as _typing
import schemas as _schemas
import services as _services

router = _fastapi.APIRouter()

@router.post("/SMC_categories/{category_id}/SMC_products/", response_model=_schemas.Product)
def create_product(
    category_id: int,
    product: _schemas.ProductCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    # db_category = _services.get_category(db=db, id=category_id)
    return _services.create_product(db=db, product=product, cat_id=category_id)

@router.get("/SMC_products/", response_model=_typing.List[_schemas.Product])
def read_products(db: _orm.Session = _fastapi.Depends(_services.get_db), skip: int = 0, limit: int = 1000):
    logs = _services.get_product(db=db, skip=skip, limit=limit)
    return logs

@router.get("/SMC_products/{id}", response_model=_schemas.Product)
def read_product(id: int = _fastapi.Path(..., description="The ID of the product you want to retrieve.", gt = 0), \
    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    logs = _services.get_product(db=db, id=id)
    return logs


@router.delete("/SMC_products/{id}")
def delete_record(id: int = _fastapi.Path(..., description="The ID of the Record you want to delete.", gt = 0), \
    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_record(db=db, id=id, table_name="product")
    return {"message": "successfully deleted record with id: "+ str(id)}

# details table :
@router.post("/SMC_products/{product_id}/SMC_details_table/", response_model=_schemas.Details)
def create_detail(
    product_id: int,
    details: _schemas.DetailsCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    # db_product = _services.get_product(db=db, id=product_id)
    return _services.create_details(db=db, detail=details, p_id=product_id)

@router.get("/SMC_details_table/", response_model=_typing.List[_schemas.Details])
def read_details(db: _orm.Session = _fastapi.Depends(_services.get_db), skip: int = 0, limit: int = 1000):
    logs = _services.get_details(db=db, skip=skip, limit=limit)
    return logs

@router.get("/SMC_details_table/id={id}", response_model=_schemas.Product)
def read_details(id: int = _fastapi.Path(..., description="The ID of the details table you want to retrieve.", gt = 0), \
    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    logs = _services.get_details(db=db, id=id)
    return logs

@router.get("/SMC_details_table/product_id={id}", response_model=_schemas.Product)
def read_details(product_id: int = _fastapi.Path(..., description="The ID of the product you want to retrieve its results.", gt = 0), \
    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    logs = _services.get_details(db=db, product_id=product_id)
    return logs

@router.delete("/SMC_products/{id}")
def delete_record(id: int = _fastapi.Path(..., description="The ID of the Record you want to delete.", gt = 0), \
    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_record(db=db, id=id, table_name="details")
    return {"message": "successfully deleted record with id: "+ str(id)}