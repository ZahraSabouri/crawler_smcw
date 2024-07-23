import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import db_credentials as _cr


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://"+ _cr.dbuser +":"+ _cr.dbpass +"@"+ _cr.dbhost +"/"+ _cr.dbname 

engine = _sql.create_engine(SQLALCHEMY_DATABASE_URL) #, connect_args={"check_same_thread": False})

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()