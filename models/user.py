from dataclasses import dataclass, field
from datetime import datetime
import random
import string
from typing import List, Optional

@dataclass
class User:
    """User model"""
    user_id: int
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    balance: int = 0  # in stars
    total_spent: float = 0.0  # in RUB
    purchase_count: int = 0
    referral_code: str = field(default_factory=lambda: ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)))
    referral_count: int = 0
    referral_earning: float = 0.0
    level: str = "Новичок"
    achievements: List[str] = field(default_factory=list)
    
    def get_full_name(self) -> str:
        """Get user's full name"""
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name
    
    def get_mention(self) -> str:
        """Get user mention"""
        if self.username:
            return f"@{self.username}"
        return self.get_full_name()
    
    def get_joined_date(self) -> str:
        """Get formatted joined date"""
        return self.created_at.strftime("%d.%m.%Y")
    
    def update_level(self):
        """Update user level based on spending"""
        if self.total_spent >= 50000:
            self.level = "🏆 Легенда"
        elif self.total_spent >= 20000:
            self.level = "💎 Премиум"
        elif self.total_spent >= 10000:
            self.level = "⭐ Профессионал"
        elif self.total_spent >= 5000:
            self.level = "✨ Продвинутый"
        elif self.total_spent >= 1000:
            self.level = "🌟 Активный"
        else:
            self.level = "👤 Новичок"

@dataclass
class Transaction:
    """Transaction/Purchase record"""
    transaction_id: str
    user_id: int
    stars: int
    price: float  # in RUB
    payment_method: str  # 'card', 'yandex', 'crypto', etc
    status: str  # 'pending', 'completed', 'failed'
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None
    
    def get_formatted_date(self) -> str:
        """Get formatted date"""
        return self.created_at.strftime("%d.%m.%Y %H:%M")
    
    def get_status_emoji(self) -> str:
        """Get status emoji"""
        if self.status == 'completed':
            return '✅'
        elif self.status == 'pending':
            return '⏳'
        else:
            return '❌'
