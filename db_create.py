from app import db
from models import BlogPost

# create tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m Well."))
db.session.add(BlogPost("postgres", "We setup a local postgres database."))
db.session.add(BlogPost("mac", "postgres instance on mac."))

db.session.commit()