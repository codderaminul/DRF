from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post,Category

class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='Python')
        testuser1 = User.objects.create_user(username='admin',password='admin')
        testpost = Post.objects.create(category_id=1,title='Post Title',excerpt='Post excerpt',content="Post content",slug="Post-Slug",author_id=1,status='published')

    def test_blog_content(self):
        cat = Category.objects.get(id=1)
        post = Post.postobject.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        content = f'{post.content}'
        title = f'{post.title}'
        status = f'{post.status}'
        self.assertEqual(author,'admin')
        self.assertEqual(excerpt,'Post excerpt')
        self.assertEqual(content,'Post content')
        self.assertEqual(title,'Post Title')
        self.assertEqual(status,'published')
        self.assertEqual(str(post),'Post Title')
        self.assertEqual(str(cat),'Python')








