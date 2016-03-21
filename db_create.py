from app import db
from models import BlogPost

# create tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m Well."))

db.session.commit()