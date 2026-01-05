from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel
from app.routes import transactions

# Important Notes: This file has changes until 6.12 without structured routes added.
# The routes have been moved to app/routes/transactions.py for better organization.

# class Transaction(BaseModel):
#     type: str
#     amount: float
#     description: str


# app = FastAPI()

# @app.get("/")
# def root():
#     return {"message": "FastAPI is working!"}

# @app.get("/hello")
# def say_hello():
#     return {"message": "Hello from FastAPI"}

# # This method will accept all the input datas without validing the input format
# @app.post("/echo")
# def echo_data(data: dict = Body(...)):
#     return {
#         "you_sent": data
#     }

# # This method will accept only valid input datas according to the Transaction model
# @app.post("/transaction")
# def create_transaction(transaction: Transaction):
#     return {
#         "status": "success",
#         "transaction": transaction
#     }
