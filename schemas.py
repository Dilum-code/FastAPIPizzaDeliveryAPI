from pydantic import BaseModel
from typing import List
from models import PizzaSize, OrderStatus

class PizzaBase(BaseModel):
    name: str
    ingredients: str
    price: float
    size: PizzaSize

class PizzaCreate(PizzaBase): pass

class Pizza(PizzaBase):
    id: int
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    pizza_id: int
    customer_name: str
    address: str
    status: OrderStatus

class OrderCreate(OrderBase): pass

class Order(OrderBase):
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

from pydantic import BaseModel
from models import PizzaSize

class PizzaCreate(BaseModel):
    name: str
    ingredients: str
    price: float
    size: PizzaSize

class Pizza(PizzaCreate):
    id: int
    class Config:
        from_attributes = True


