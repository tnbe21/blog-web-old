import time
from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text
    )

from . import Base


class Article(Base):
    __tablename__ = 'article'
    article_id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(String(50), nullable=False)
    body = Column(Text, nullable=False)
    # 0: DRAFT, 1: PUBLIC, 10: PRIVATE
    status = Column(Integer, nullable=False)
    create_dt = Column(Integer, nullable=False, default=int(time.mktime(datetime.now().timetuple())))
    update_dt = Column(Integer, nullable=False, default=int(time.mktime(datetime.now().timetuple())))
