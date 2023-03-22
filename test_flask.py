from unittest import TestCase

from app import app
from models import db, User, Post, Tag, PostTag


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = True

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class BloglyTestCase(TestCase):
    """test for model of users"""

    def setUp(self):
        """Clean up any existing users"""

        
        PostTag.query.delete()
        Tag.query.delete()
        Post.query.delete()
        User.query.delete()

        user = User(first_name='Skate', last_name="board", image_url='data:image/jpeg;base64,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')
        db.session.add(user)
        db.session.commit()
       
        self.user_id = user.id

        post = Post(title="they call me smelly", content="they call me smelly goondie but im  really not that smelly", user_id=self.user_id)
        db.session.add(post)
        db.session.commit()

        self.post_id = post.id

        tag = Tag(name = "dogsRule")
        db.session.add(tag)
        db.session.commit()

        self.tag_id = tag.id


        pt1 = PostTag(post_id = self.post_id, tag_id = self.tag_id)

        db.session.add(pt1)
        db.session.commit()

        



    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_home(self):
        with app.test_client() as client:
            response = client.get('/')

            self.assertEqual(response.status_code, 302)

    def test_users(self):
        with app.test_client() as client:
            response= client.get('/users')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('>Add User</a>',html)

    def test_new_user(self):
        with app.test_client() as client:
            response = client.get("users/new")
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Create new user</h1>', html)
    
    def test_edit_user(self):
        with app.test_client() as client:
            response = client.get("users/1/edit")
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Edit user</h1>', html)
    
    def test_new_user_post(self):
        with app.test_client() as client:
            d = {'first_name':"Smelly", "last_name":"the Dog","image_url":"fake_url.jpg"}
            response = client.post("/users/new", data = d, follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('>Smelly the Dog</a>', html)
   
    def test_edit_user_post(self):
        with app.test_client() as client:
            d = {'first_name':"Skate", "last_name":"the board","image_url":"better_image.jpg"}
            response = client.post(f'/users/{self.user_id}/edit', data = d, follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('>Skate the board</a>', html)
 
    def test_delete_user_post(self):
        with app.test_client() as client:
            response = client.post(f'/users/{self.user_id}/delete', follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('>Add User</a>', html)

    def test_new_post_form(self):
        with app.test_client() as client:
            response = client.get(f'/users/{self.user_id}/posts/new')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h2>Add Post for ', html)

    def test_posted_new_post(self):
        with app.test_client() as client:
            d = {'title':"Sssup Ssuckersss", 'content':"Ssslimeyss back at it again sssuckersss", 'user_id': f'{self.user_id}'}
            response = client.post(f'/users/{self.user_id}/posts/new', data = d, follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('>Sssup Ssuckersss</a>', html)

    def test_post_page(self):
        with app.test_client() as client:
            response = client.get(f'/posts/{self.post_id}')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h2>they call me smelly</h2>', html)

    def test_edit_form(self):
        with app.test_client() as client:
            response = client.get(f'/posts/{self.post_id}/edit')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h2>Edit Post</h2>', html)

    def test_posted_edited_post(self):
        with app.test_client() as client:
            d = {'title':"Sssup boi", 'content':"Ssslimeyss back at it again sssuckersss", 'user_id': f'{self.user_id}'}
            response = client.post(f'/posts/{self.post_id}/edit', data = d, follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('>Sssup boi</a>', html)

    def test_delete_post(self):
        with app.test_client() as client:
            response = client.post(f'/posts/{self.post_id}/delete', follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h2>Skate board</h2>', html)

    def test_show_tags(self):
        with app.test_client() as client:
            response = client.get(f'/tags')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h2>Tags</h2>', html)
 
    def test_show_single_tag(self):
        with app.test_client() as client:
            response = client.get(f'/tags/{self.tag_id}')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h3>dogsRule</h3>', html)
   
    def test_new_tag_form(self):
        with app.test_client() as client:
            response = client.get(f'/tags/new')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Create new tag</h1>', html)

    def test_posted_tag(self):
        with app.test_client() as client:
            d = {'tag': 'catsRule'}
            response = client.post(f'/tags/new', data = d, follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('>catsRule</a>', html)
   
    def test_edit_tag_form(self):
        with app.test_client() as client:
            response = client.get(f'/tags/{self.tag_id}/edit')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Edit tag</h1>', html)


    def test_posted_edit_tag(self):
        with app.test_client() as client:
            d = {'tag': 'miceRule'}
            response = client.post(f'/tags/{self.tag_id}/edit', data = d, follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('>miceRule</a>', html)
   
    def test_delete_tag(self):
        with app.test_client() as client:
            response = client.post(f'/tags/{self.tag_id}/delete', follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h2>Tags</h2>', html)