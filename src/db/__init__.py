from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from .Channels import Channels
from .Roles import Roles
from .Servers import Servers
from .Users import Users
