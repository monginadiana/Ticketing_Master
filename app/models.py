from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

class Theater(Base):
    __tablename__ = "theaters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    seats = Column(Integer)

class Seating(Base):
    __tablename__ = "seatings"
    id = Column(Integer, primary_key=True, index=True)
    theater_id = Column(Integer, ForeignKey("theaters.id"))
    date = Column(DateTime)
    theater = relationship("Theater")

class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True, index=True)
    seating_id = Column(Integer, ForeignKey("seatings.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    seat_number = Column(Integer)
    seating = relationship("Seating")
    user = relationship("User")
