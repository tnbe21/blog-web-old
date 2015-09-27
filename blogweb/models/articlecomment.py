import time
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
    )

from . import Base


class ArticleComment(Base):
    __tablename__ = 'article_comment'
    comment_id = Column(Integer, primary_key=True, autoincrement=False)
    article_id = Column(Integer, primary_key=True, autoincrement=False)
    body = Column(Text, nullable=False)
    author = Column(String(30), nullable=False, default='')
    # 1: PUBLIC, 10: PRIVATE
    status = Column(Integer, nullable=False)
    create_dt = Column(Integer, nullable=False, default=int(time.mktime(datetime.now().timetuple())))
    update_dt = Column(Integer, nullable=False, default=int(time.mktime(datetime.now().timetuple())))