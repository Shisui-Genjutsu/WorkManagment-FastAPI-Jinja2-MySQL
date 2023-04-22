from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(VARCHAR(300), unique=True, index=True)
    username = Column(VARCHAR(300), unique=True, index=True)
    first_name = Column(VARCHAR(300))
    last_name = Column(VARCHAR(300))
    hashed_password = Column(VARCHAR(300))
    is_active = Column(Boolean, default=True)

    todos = relationship("Todos", back_populates="owner")


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(300))
    description = Column(VARCHAR(300))
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="todos")
