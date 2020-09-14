from sqlalchemy import ForeignKey, Column, BigInteger, Boolean, Text
from . import Base

class Warnings(Base):
    __tablename__ = 'warnings'
    id = Column(BigInteger, primary_key = True)

    # the moderator who performed the warning
    # will be the bot's id if an automated warning
    # was generated
    moderator_id = Column(BigInteger, nullable=False, index=True)

    # the user who was warned
    user_id = Column(BigInteger, nullable=False, index=True)

    # which server the warning was associated with
    server_id = Column(BigInteger, nullable=False, index=True)

    # which chanenl, if any, the warning was associated with
    server_id = Column(BigInteger, nullable=True, index=True)

    # the text of the warning that provides context
    context = Column(Text, default='')

    # was this warning accompanied by a kick?
    kicked = Column(Boolean, nullable=False, default=False)

    # was this warning accompanied by a ban?
    banned = Column(Boolean, nullable=False, default=False)
