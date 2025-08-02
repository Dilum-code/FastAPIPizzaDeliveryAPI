from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import get_db
import crud, schemas

from auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user,
    get_db,
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register
@app.post("/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_pw = get_password_hash(user.password)
    return crud.create_user(db, user, hashed_pw)

# Login
@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

# Secure route example
@app.get("/me", response_model=schemas.User)
def read_current_user(current_user: schemas.User = Depends(get_current_user)):
    return current_user

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/pizzas", response_model=list[schemas.Pizza])
def list_pizzas(db: Session = Depends(get_db)):
    return crud.get_pizzas(db)

@app.get("/pizza/{name}", response_model=schemas.Pizza)
def get_pizza(name: str, db: Session = Depends(get_db)):
    pizza = crud.get_pizza_by_name(db, name)
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return pizza

@app.post("/pizzas", response_model=schemas.Pizza)
def add_pizza(pizza: schemas.PizzaCreate, db: Session = Depends(get_db)):
    return crud.create_pizza(db, pizza)

@app.post("/order", response_model=schemas.Order)
def order_pizza(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@app.get("/orders", response_model=list[schemas.Order])
def list_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)

@app.put("/order/{order_id}/status", response_model=schemas.Order)
def update_order(order_id: int, status: models.OrderStatus, db: Session = Depends(get_db)):
    order = crud.update_order_status(db, order_id, status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.get("/users", response_model=list[schemas.User])
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.post("/pizzas", response_model=schemas.Pizza)
def create_pizza(pizza: schemas.PizzaCreate, db: Session = Depends(get_db)):
    return crud.create_pizza(db, pizza)


