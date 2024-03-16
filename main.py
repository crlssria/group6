from fastapi import FastAPI, HTTPException, Query, Body, Header
from fastapi.responses import HTMLResponse  # Add this import
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection string
MONGO_URI = "mongodb+srv://mcassoria:carlossoria40@cluster0.omh8hwv.mongodb.net/"

# MongoDB database name
DATABASE_NAME = "record"

# Secret key
SECRET_KEY = "group6"

app = FastAPI()

# Connect to MongoDB with SSL and CA certificate
client = MongoClient(MONGO_URI)

# MongoDB database and collections
db = client[DATABASE_NAME]
sales_collection = db["sales"]  # Collection for sales records

# Route to serve index.html
@app.get("/", response_class=HTMLResponse)
async def get_html():
    try:
        with open("index.html", "r") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Index file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route to handle the report request
@app.get("/report")
async def get_report(X_Secret_Key: str = Query(..., alias="X-Secret-Key")):
    if X_Secret_Key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
   
    # Fetch sales report from the database
    sales_report = list(sales_collection.find({}, {"_id": 0, "product": 1}))
    return {"sales_report": sales_report}

# Route to handle the buy request
@app.post("/buy")
async def buy_product(product_info: dict = Body(...), x_secret_key: str = Header(None)):
    try:
        if x_secret_key != SECRET_KEY:
            raise HTTPException(status_code=401, detail="Unauthorized")
        
        product_name = product_info.get("product")
        if not product_name:
            raise HTTPException(status_code=422, detail="Product name missing in request")
        
        # Generate timestamp
        timestamp = datetime.now()
        
        # Insert the purchase record into the database with the timestamp
        sales_collection.insert_one({"product": product_name, "timestamp": timestamp})
        return {"message": f"Successfully purchased {product_name}"}
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# MongoDB connection string
MONGO_URI = "mongodb+srv://mcassoria:carlossoria40@cluster0.omh8hwv.mongodb.net/"

# MongoDB database name
DATABASE_NAME = "record"

# Secret key
SECRET_KEY = "group6"

app = FastAPI()

# Connect to MongoDB with SSL and CA certificate
client = MongoClient(MONGO_URI)

# MongoDB database and collections
db = client[DATABASE_NAME]
sales_collection = db["sales"]  # Collection for sales records

# Route to serve index.html
@app.get("/", response_class=HTMLResponse)
async def get_html():
    try:
        with open("index.html", "r") as file:
            html_content = file.read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Index file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Route to handle the report request
@app.get("/report")
async def get_report(X_Secret_Key: str = Query(..., alias="X-Secret-Key")):
    if X_Secret_Key != SECRET_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
   
    # Fetch sales report from the database
    sales_report = list(sales_collection.find({}, {"_id": 0, "product": 1}))
    return {"sales_report": sales_report}

# Route to handle the buy request
@app.post("/buy")
async def buy_product(product_info: dict = Body(...), x_secret_key: str = Header(None)):
    try:
        if x_secret_key != SECRET_KEY:
            raise HTTPException(status_code=401, detail="Unauthorized")
        
        product_name = product_info.get("product")
        if not product_name:
            raise HTTPException(status_code=422, detail="Product name missing in request")
        
        # Generate timestamp
        timestamp = datetime.now()
        
        # Insert the purchase record into the database with the timestamp
        sales_collection.insert_one({"product": product_name, "timestamp": timestamp})
        return {"message": f"Successfully purchased {product_name}"}
    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
