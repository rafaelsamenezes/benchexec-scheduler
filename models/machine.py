from sqlalchemy import Column, Integer, String, Boolean
from db import Base

class Machine(Base):
    __tablename__ = "machines"

    pk_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    is_active = Column(Boolean)

    def __repr__(self):
        return "<Machine (name='%s', address='%s', is_active='%s')>" % (self.name, self.address, self.is_active)
