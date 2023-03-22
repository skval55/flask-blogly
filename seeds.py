
from models import User, db, Post, Tag, PostTag
from app import app

# Create all tables
db.drop_all()
db.create_all()

User.query.delete()

u1 = User(first_name='Smelly', last_name='Goondie')
u2 = User(first_name='Slimy', last_name='Salamander', image_url='https://preview.redd.it/c15r3byfed851.jpg?auto=webp&s=936a10dad6d9045787cca9d73a5f5f5373994ec3')
u3 = User(first_name='Barky', last_name='Dogomode', image_url='https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/51tYXyD5NHL._AC_UF1000,1000_QL80_.jpg')
u4 = User(first_name='Fred', last_name='', image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5fmVxXCDsDe3ZCyAc8jyROdRvwG4H5qlYFgbFGsQyGKfnEiv3fhqKH6gGsQoWB4-KkAM&usqp=CAU')

db.session.add_all([u1, u2, u3, u4])
db.session.commit()

p1 = Post(title="they call me smelly", content="they call me smelly goondie but im  really not that smelly", user_id=1)
p2 = Post(title="Sssup Ssuckersss", content="Ssslimeyss back at it again sssuckersss", user_id=2)
p3 = Post(title="really!", content="Trust me guys! I'm really not that smelly!", user_id=1)
p4 = Post(title="Sup Chumps", content="Bark Bark Chumps", user_id=4)

db.session.add_all([p1, p2, p3, p4])
db.session.commit()

dogs_rule = Tag(name = "dogsRule")
db.session.add(dogs_rule)
db.session.commit()

pt1 = PostTag(post_id = 4, tag_id = 1)

db.session.add(pt1)
db.session.commit()
