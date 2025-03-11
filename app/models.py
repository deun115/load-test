from typing import Optional

from sqlalchemy import DateTime, Integer, PrimaryKeyConstraint, Column
from sqlalchemy.orm import Mapped
from sqlalchemy.ext.declarative import declarative_base

import datetime

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = 'user_info'
    __table_args__ = (
        PrimaryKeyConstraint('user_id', name='user_info_pkey'),
    )

    user_id: Mapped[int] = Column(Integer, primary_key=True)
    item_id: Mapped[int] = Column(Integer)
    created_at: Mapped[datetime.datetime] = Column(DateTime)
    updated_at: Mapped[Optional[datetime.datetime]] = Column(DateTime)
