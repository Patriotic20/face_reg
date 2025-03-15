from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import ARRAY , FLOAT
from src.core.base import Base

class KnownFace(Base):
    __tablename__ = "knownfaces"

    id = Column(Integer , primary_key=True , nullable=False , index=True)
    last_name = Column(String, nullable=False, index=True)
    first_name = Column(String, nullable=False, index=True)
    encoding = Column(ARRAY(FLOAT))