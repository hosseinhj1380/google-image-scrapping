from sqlalchemy import create_engine, Column, Integer, String,Boolean,select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to the PostgreSQL database
engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/rest_project')

class Base (DeclarativeBase):
    pass

class rest_db_sql(Base):
    __tablename__ = 'app_scrap_request'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    quantity = Column(Integer)
    readed=Column(Boolean)
# Query all users

# def request_from_sql():
#     requests = session.query(rest_db).filter(rest_db.readed=='false')
#     for req in requests:
#         print(req.title)
#         req.readed=True
#         session.commit()
#     # return requests
#     session.close()


if __name__=='__main__' :
    request_from_sql()
