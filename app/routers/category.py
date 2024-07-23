from re import U
import fastapi as _fastapi
from sqlalchemy import orm as _orm
import typing as _typing
import schemas as _schemas
import services as _services

router = _fastapi.APIRouter()

@router.post("/SMC_categories/", response_model=_schemas.Category)
def create_category(category: _schemas.CategoryCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return _services.create_category(db=db, category=category)

@router.get("/SMC_categories/", response_model=_typing.List[_schemas.Category])
def read_categories(db: _orm.Session = _fastapi.Depends(_services.get_db), skip: int = 0, limit: int = 1000):
    logs = _services.get_category(db=db, skip=skip, limit=limit)
    return logs

@router.get("/SMC_categories/{id}", response_model=_schemas.Category)
def read_category(id: int = _fastapi.Path(..., description="The ID of the category you want to retrieve.", gt = 0), \
    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    logs = _services.get_category(db=db, id=id)
    return logs

@router.delete("/SMC_categories/{id}")
def delete_record(id: int = _fastapi.Path(..., description="The ID of the Record you want to delete.", gt = 0), \
    db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_record(db=db, id=id, table_name="category")
    return {"message": "successfully deleted record with id: "+ str(id)}