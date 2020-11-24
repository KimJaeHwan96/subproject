from test_plus.test import TestCase, APITestCase
from rest_framework import status
from board.models import Post, Member


class PostLogInAPITest(APITestCase):
    def setUp(self):
        self.kim = self.make_user(username='kim', password='password')
        self.jae = self.make_user(username='jae', password='password')

    def test_get_posts_list(self):
        response = self.client.get(self.reverse(name='-list'))
        assert response.status_code == status.HTTP_200_OK

    def test_get_posts_detail(self):
        #post = Post.objects.create()
        response = self.client.get(self.reverse(name='-detail', pk=1))
        self.response_404(response)

    def test_put_posts(self):
        data = {
            "title": "test2",
            "description": "Django Rest Framework",
            "writer": "2"
        }
        response = self.client.put(self.reverse(name='-detail', pk=2), data=data)
        self.response_403(response)


class PostLogOutAPITest(APITestCase):

    def test_get_posts_list(self):
        response = self.client.get(self.reverse(name='-list'))
        assert response.status_code == status.HTTP_200_OK

    def test_get_posts_detail(self):
        #post = Post.objects.create()
        response = self.client.get(self.reverse(name='-detail', pk=1))
        self.response_404(response)

    def test_put_posts(self):
        data = {
            "title": "test2",
            "description": "Django Rest Framework",
            "writer": "2"
        }
        response = self.client.put(self.reverse(name='-detail', pk=2), data=data)
        self.response_403(response)
