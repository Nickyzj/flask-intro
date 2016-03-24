from project import db
from project.models import User

db.session.add(User("michael", "michael@realpython.com", "i will never tell"))
db.session.add(User("admin2", "admin2@ad.com", "admin"))

db.session.commit()