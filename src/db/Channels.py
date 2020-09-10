from sqlalchemy import ForeignKey, Column, Boolean, Integer, String, JSON
from . import Base

class Channels(Base):
    __tablename__ = 'channels'
    id = Column(Integer, primary_key = True)

    # override the Global and Server prefixes with a custom
    # prefix specific to this channel
    prefix = Column(String(10), nullable=True)

    # Ignore interactions in this channel,
    # muted and voiced cannot both be True
    muted = Column(Boolean, nullable=False, default=False)

    # Specifically allow interactions in this channel
    # Only useful when server is globally muted such as
    # you only want 1 channel for bot interactions
    # muted and voiced cannot both be True
    voiced = Column(Boolean, nullable=False, default=False)

    # Storing Ad-hoc data made easy
    jsondata = Column(JSON)
