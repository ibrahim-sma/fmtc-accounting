
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.transaction import Transaction
from app.core.dependencies import get_current_user


router = APIRouter()

class TransactionCreate(BaseModel):
    type: str
    amount: float
    description: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transaction")
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    db_transaction = Transaction(
        type=transaction.type,
        amount=transaction.amount,
        description=transaction.description
    )
    if user.get("role") != "admin":
        raise Exception("Only admin users can create transactions.")
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)

    return db_transaction

@router.get("/transactions")
def list_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions

@router.get("/transaction/{transaction_id}")
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    return transaction

@router.delete("/transaction/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction:
        db.delete(transaction)
        db.commit()
        return {"message": "Transaction deleted successfully"}
    return {"message": "Transaction not found"}

@router.put("/transaction/{transaction_id}")
def update_transaction(
    transaction_id: int,
    transaction_data: TransactionCreate,
    db: Session = Depends(get_db)
):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction:
        transaction.type = transaction_data.type
        transaction.amount = transaction_data.amount
        transaction.description = transaction_data.description
        db.commit()
        db.refresh(transaction)
        return transaction
    return {"message": "Transaction not found"}

@router.get("/summary")
def transaction_summary(db: Session = Depends(get_db)):
    income = db.query(Transaction).filter(Transaction.type == "income").all()
    expense = db.query(Transaction).filter(Transaction.type == "expense").all()

    total_income = sum(t.amount for t in income)
    total_expense = sum(t.amount for t in expense)

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense
    }
