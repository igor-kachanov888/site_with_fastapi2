import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

metadata = sqlalchemy.MetaData()

from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

from sqlalchemy.orm import sessionmaker

class Users_table(DeclarativeBase):
    __tablename__ = 'users'
    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True)
    email = sqlalchemy.Column("email", sqlalchemy.String(40), unique=True, index=True)
    name = sqlalchemy.Column("name", sqlalchemy.String(100))
    hashed_password = sqlalchemy.Column("hashed_password", sqlalchemy.String())

    is_active = sqlalchemy.Column(
                                    "is_active",
                                    sqlalchemy.Boolean(),
                                    server_default=sqlalchemy.sql.expression.true(),
                                    nullable=False,
                                )

    def __repr__(self):
        return "".format(self.code)


"""
users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(40), unique=True, index=True),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
    sqlalchemy.Column("hashed_password", sqlalchemy.String()),
    sqlalchemy.Column(
        "is_active",
        sqlalchemy.Boolean(),
        server_default=sqlalchemy.sql.expression.true(),
        nullable=False,
    ),
)

"""

tokens_table = sqlalchemy.Table(
    "tokens",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "token",
        UUID(as_uuid=False),
        unique=True,
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("expires", sqlalchemy.DateTime()),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id")),
)
'''
#sqlalchemy.url = driver://user:pass@localhost/dbname
'''
if __name__ == "__main__":
    engine = sqlalchemy.create_engine("postgresql+psycopg2://user:2@localhost/fastAPItest")
    metadata.create_all(engine)
