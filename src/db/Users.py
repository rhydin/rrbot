from sqlalchemy import ForeignKey, Column, Boolean, Integer, String, JSON
from . import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, autoincrement=False)

    # Allows this user to interact with this bot even if a
    # channel or server are muted.
    # muted and voiced cannot both be True
    voiced = Column(Boolean, nullable=False, default=False)

    # Prevents this user from interacting with the bot at all.
    # muted and voiced cannot both be True
    muted = Column(Boolean, nullable=False, default=False)

    # Specifies this user as able to use moderation all tools
    moderator = Column(Boolean, nullable=False, default=False)

    # Storing Ad-hoc data made easy
    jsondata = Column(JSON)
