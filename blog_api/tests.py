from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from blog.models import Category,Post


class PostTests(APITestCase):
    def post_view_test(self):
        url = reverse('blog_api:listcreate')
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def create_post(self):
        self.test_category = Category.objects.create(name='Python')
        self.testuser1 = User.objects.create_user(username='admin', password='admin')

        data = {"title":"new","author":1,"excerpt":"new excerpt","content":"new"}
        url = reverse('blog_api:listcreate')
        response = self.client.get(url, data,format='json')















