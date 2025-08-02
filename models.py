from sqlalchemy import Column, Integer, String, Float, Enum
from database import Base
import enum

class PizzaSize(str, enum.Enum):
    small = "small"
    medium = "medium"
    large = "large"

class OrderStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    delivered = "delivered"
    cancelled = "cancelled"

class Pizza(Base):
    __tablename__ = "pizzas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(String)
    price = Column(Float)
    size = Column(Enum(PizzaSize))

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    pizza_id = Column(Integer)
    customer_name = Column(String)
    address = Column(String)
    status = Column(Enum(OrderStatus))

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

