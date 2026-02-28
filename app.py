from fastapi import FastAPI , Depends
from models import product
from database import session, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")

def greet():
    return "HI, This is Prad"

products = [
    product(id=1,name="phone",description="budget phone",price=89,quantity=20),
    product(id=2,name="laptop",description="gaming laptop",price=999,quantity=50),
    product(id=3,name="Headphones",description="gaming headphones",price=119.99,quantity=70),
    product(id=4,name="table",description="laptop table",price=69.99,quantity=120)
]

def init_db():
    db = session()
    count = db.query(database_models.product).count

    if count == 0:
        for product in products:
            db.add(database_models.product(**product.model_dump()))
            db.commit()

init_db()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/products")

def get_all_products(db: Session = Depends(get_db)):
    
    db_products = db.query(database_models.product).all()

    return db_products
    db.commit()

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"

@app.post("/product")
def add_product(product:product):
     products.append(product)
     return product


@app.put("/product")
def update_product(id:int,product:product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated successfully"
    return "product not found"


@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted"
    return "product not found"
