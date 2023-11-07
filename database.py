from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine = create_engine('mysql+pymysql://root:1234@localhost:3306/pizza_delivery')

Base=declarative_base()

Session=sessionmaker()