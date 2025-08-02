from sqlalchemy.orm import Session
import models, schemas

def get_pizzas(db: Session):
    return db.query(models.Pizza).all()

def get_pizza_by_name(db: Session, name: str):
    return db.query(models.Pizza).filter(models.Pizza.name.ilike(name)).first()

def create_pizza(db: Session, pizza: schemas.PizzaCreate):
    db_pizza = models.Pizza(**pizza.dict())
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session):
    return db.query(models.Order).all()

def update_order_status(db: Session, order_id: int, status: models.OrderStatus):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order:
        order.status = status
        db.commit()
        db.refresh(order)
    return order

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


