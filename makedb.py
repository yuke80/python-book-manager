import os
from sqlalchemy import create_engine

# engine = create_engine('sqlite:///:memory:', echo=False)
# engine = create_engine('sqlite:///book.db', echo=False)
db = os.path.dirname(__file__) + "/book.db" # For VScode
engine = create_engine('sqlite:///'+db, echo=True)

from sqlalchemy import Column, Integer, Unicode, UnicodeText
import sqlalchemy
version = sqlalchemy.__version__.split('.')
if int(version[0]) < 2:
    from sqlalchemy.ext import declarative
    Base = declarative.declarative_base() # sqlalchemy ver1.4.x
else:
    Base = sqlalchemy.orm.declarative_base() # sqlalchemy ver2.0.x

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(100), nullable=False)
    price = Column(Integer, nullable=False)
    memo = Column(UnicodeText)
    def __repr__(self):
        return "<Book('%s', '%s', '%s')>" % (self.title, self.price, self.memo)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([
    Book(title= 'Pythonチュートリアル', price='1800', memo = 'Guido van Rossum'),
    Book(title= 'やさしいPython', price='2580', memo = '高橋麻奈'),
    Book(title= 'Pythonによる機械学習入門', price='2600', memo = '株式会社システム計画研究所'),
    ])
session.commit()