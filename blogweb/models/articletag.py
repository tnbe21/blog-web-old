import time
from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer
)

from . import Base


class ArticleTag(Base):
    __tablename__ = 'article_tag'
    article_id = Column(Integer, ForeignKey('article.article_id'), primary_key=True, autoincrement=False)
    tag_id = Column(Integer, ForeignKey('tag.tag_id'), primary_key=True, autoincrement=False)
    create_dt = Column(Integer, nullable=False)
    update_dt = Column(Integer, nullable=False)

    def __init__(self):
        self.create_dt = int(time.mktime(datetime.now().timetuple()))
        self.update_dt = int(time.mktime(datetime.now().timetuple()))
