from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///ac_tracker.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

class Unit(Base):
    __tablename__ = "units"
    id = Column(Integer, primary_key=True, index=True)
    facility = Column(String, index=True)
    tenant = Column(String)
    manufacturer = Column(String)
    model_number = Column(String)
    serial_number = Column(String)
    tonnage = Column(Float)
    seer = Column(Float)
    heat = Column(String)
    status = Column(String)
    last_service = Column(Date)

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    unit_id = Column(Integer, index=True)
    issue = Column(String)
    part = Column(String)
    repair_status = Column(String)
    check_date = Column(Date)
    date_repaired = Column(Date)
    cost = Column(Float)

Base.metadata.create_all(bind=engine)
