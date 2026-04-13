from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tweet_id = Column(String(100), unique=True, nullable=False)
    username = Column(String(100))
    full_name = Column(String(200))
    content = Column(Text)
    post_url = Column(String(300))
    post_date = Column(String(100))
    screenshot = Column(LargeBinary)  # binary image data
    scraped_at = Column(DateTime, default=datetime.utcnow)

engine = create_engine(
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def save_post(session, tweet_data, screenshot_bytes):
    post = Post(
        tweet_id=tweet_data['tweet_id'],
        username=tweet_data['username'],
        full_name=tweet_data['full_name'],
        content=tweet_data['content'],
        post_url=tweet_data['post_url'],
        post_date=tweet_data['post_date'],
        screenshot=screenshot_bytes
    )
    session.add(post)
    session.commit()
    print(f"Saved post from @{tweet_data['username']}")