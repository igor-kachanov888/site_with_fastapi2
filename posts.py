import sqlalchemy
import datetime
from models.users import Users_table
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

from sqlalchemy.orm import sessionmaker

class Post(DeclarativeBase):
    __tablename__ = 'posts'
    id = sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True)
    user_id = sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(Users_table.id))
    created_at = sqlalchemy.Column("created_at", sqlalchemy.DateTime())
    title = sqlalchemy.Column("title", sqlalchemy.String(100))
    content = sqlalchemy.Column("content", sqlalchemy.Text())

    def __repr__(self):
        return "".format(self.content)

def add_post(content, user_id = 0, title = "", email=None):
    engine = sqlalchemy.create_engine("postgresql+psycopg2://user:2@localhost/fastAPItest")
    Session = sessionmaker(bind=engine)
    session = Session()
    users = [user for user in session.query(Users_table)]
    if email is None:
        email = title
    is_creating_users = True
    for user in users:
        if email == user.email:
            user_id = user.id
            is_creating_users = False
            break

    if is_creating_users:
        new_user = Users_table(email=email,
                               name="",
                               hashed_password="",
                               is_active=True
                               )
        session.add(new_user)
        session.commit()

    user = session.query(Users_table).filter_by(email=email).all()[0]

    new_post = Post(user_id=user.id,
                    created_at=datetime.datetime.now(),
                    title=title,
                    content=content)
    session.add(new_post)
    session.commit()

    # А теперь попробуем вывести все посты , которые есть в нашей таблице
    for post in session.query(Post):
        print(post)

    print("ADD POST OK!")




"""
posts_table = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey(users_table.c.id)),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("title", sqlalchemy.String(100)),
    sqlalchemy.Column("content", sqlalchemy.Text()),
)
"""
if __name__ == "__main__":
    metadata = sqlalchemy.MetaData()
    engine = sqlalchemy.create_engine("postgresql+psycopg2://user:2@localhost/fastAPItest")

    metadata.create_all(engine)