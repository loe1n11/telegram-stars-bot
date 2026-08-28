"""User database handler"""
import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from models.user import User, Transaction

# Simple JSON-based database for demo
USERS_DB = 'data/users.json'
TRANSACTIONS_DB = 'data/transactions.json'

def ensure_db_exists():
    """Create data directory if it doesn't exist"""
    os.makedirs('data', exist_ok=True)
    if not os.path.exists(USERS_DB):
        with open(USERS_DB, 'w', encoding='utf-8') as f:
            json.dump({}, f)
    if not os.path.exists(TRANSACTIONS_DB):
        with open(TRANSACTIONS_DB, 'w', encoding='utf-8') as f:
            json.dump({}, f)

def get_user(user_id: int) -> Optional[User]:
    """Get user by ID"""
    ensure_db_exists()
    try:
        with open(USERS_DB, 'r', encoding='utf-8') as f:
            users = json.load(f)
        if str(user_id) in users:
            data = users[str(user_id)]
            return User(
                user_id=user_id,
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                username=data.get('username'),
                created_at=datetime.fromisoformat(data.get('created_at', datetime.now().isoformat())),
                balance=data.get('balance', 0),
                total_spent=data.get('total_spent', 0.0),
                purchase_count=data.get('purchase_count', 0),
                referral_code=data.get('referral_code'),
                referral_count=data.get('referral_count', 0),
                referral_earning=data.get('referral_earning', 0.0),
                level=data.get('level', 'Новичок'),
                achievements=data.get('achievements', [])
            )
    except Exception as e:
        print(f"Error reading user: {e}")
    return None

def create_user(user_id: int, first_name: str, last_name: Optional[str] = None, username: Optional[str] = None) -> User:
    """Create new user"""
    ensure_db_exists()
    user = User(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        username=username
    )
    save_user(user)
    return user

def save_user(user: User):
    """Save user to database"""
    ensure_db_exists()
    try:
        with open(USERS_DB, 'r', encoding='utf-8') as f:
            users = json.load(f)
        
        users[str(user.user_id)] = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'created_at': user.created_at.isoformat(),
            'balance': user.balance,
            'total_spent': user.total_spent,
            'purchase_count': user.purchase_count,
            'referral_code': user.referral_code,
            'referral_count': user.referral_count,
            'referral_earning': user.referral_earning,
            'level': user.level,
            'achievements': user.achievements
        }
        
        with open(USERS_DB, 'w', encoding='utf-8') as f:
            json.dump(users, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving user: {e}")

def get_user_transactions(user_id: int) -> List[Transaction]:
    """Get all transactions for a user"""
    ensure_db_exists()
    transactions = []
    try:
        with open(TRANSACTIONS_DB, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        user_trans = data.get(str(user_id), [])
        for trans in user_trans:
            transactions.append(Transaction(
                transaction_id=trans.get('transaction_id'),
                user_id=user_id,
                stars=trans.get('stars'),
                price=trans.get('price'),
                payment_method=trans.get('payment_method'),
                status=trans.get('status'),
                created_at=datetime.fromisoformat(trans.get('created_at', datetime.now().isoformat())),
                completed_at=datetime.fromisoformat(trans.get('completed_at')) if trans.get('completed_at') else None
            ))
    except Exception as e:
        print(f"Error reading transactions: {e}")
    return sorted(transactions, key=lambda x: x.created_at, reverse=True)

def add_transaction(transaction: Transaction):
    """Add new transaction"""
    ensure_db_exists()
    try:
        with open(TRANSACTIONS_DB, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        user_id_str = str(transaction.user_id)
        if user_id_str not in data:
            data[user_id_str] = []
        
        data[user_id_str].append({
            'transaction_id': transaction.transaction_id,
            'stars': transaction.stars,
            'price': transaction.price,
            'payment_method': transaction.payment_method,
            'status': transaction.status,
            'created_at': transaction.created_at.isoformat(),
            'completed_at': transaction.completed_at.isoformat() if transaction.completed_at else None
        })
        
        with open(TRANSACTIONS_DB, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error adding transaction: {e}")
