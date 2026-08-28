from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    """User model"""
    user_id: int
    first_name: str
    last_name: str = None
    username: str = None
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
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
