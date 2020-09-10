from sqlalchemy import ForeignKey, Column, Boolean, Integer, String, JSON
from . import Base

class Servers(Base):
    __tablename__ = 'servers'
    id = Column(Integer, primary_key = True)

    # override the Global prefix with a custom
    # prefix specific to this server
    prefix = Column(String(10), nullable=True)

    # Ignore interactions in server except where a channel
    # has specifically been voiced.  Useful when you want to
    # limit bot interactions to only a few channels
    muted = Column(Boolean, nullable=False, default=False)

    # Storing Ad-hoc data made easy
    jsondata = Column(JSON)
