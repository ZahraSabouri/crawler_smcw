# from http.client import HTTPException
from re import U
import fastapi as _fastapi
from sqlalchemy import orm as _orm
import services as _services
import routers.category as category_router
import routers.product as product_router 

app = _fastapi.FastAPI()
app.include_router(category_router.router)
app.include_router(product_router.router)


_services.create_database()

# async def verify_token(x_token: str = _fastapi.Header(...)):
#     if x_token != "":
#         raise HTTPException(status_code=400, detail="X-Token header invalid.")
#     return "right access token entered"
    
@app.get("/")
async def root():
    return {"message": "smc world crawler"}

@app.delete("/delete_all")
def delete_records(db: _orm.Session = _fastapi.Depends(_services.get_db), table_name: str = "all"):
    _services.delete_record(db=db, table_name=table_name)
    return {"message": "successfully deleted all records of all tables."}
