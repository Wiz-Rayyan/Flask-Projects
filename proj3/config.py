import os
from secrets import token_hex

class Config:
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or token_hex(16)
    
    # SQLite database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Bcrypt configuration for password hashing
    BCRYPT_LOG_ROUNDS = 12
    
    # Pagination settings
    POSTS_PER_PAGE = 5