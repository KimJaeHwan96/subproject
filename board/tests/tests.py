from test_plus.test import TestCase, APITestCase
from rest_framework import status
from board.models import Post, Member



class APITest(APITestCase):
    def setUp(self):
        self.kim = self.make_user(username='kim', password='password')
        self.jae = self.make_user(username='jae', password='password')

    def test_register(self):
        data = {
            "username": "test2",
            "gender" : "M",
            "tel" : "9876543210",
            "email": "example@example.com",
            "password1": "123qwe!@",
            "password2": "123qwe!@"
        }
        response = self.client.post(self.reverse('rest_register'), data=data)
        assert response.status_code == status.HTTP_201_CREATED


    def test_login(self):
        response = self.client.post(self.reverse('rest_framework:login'), data={ "username": "test1", "password": "123456!@#"})
        assert response.status_code == status.HTTP_200_OK
        #assert 'user' in response.data
        #assert 'id' in response.data
        #assert response.data['user']['username'] == 'test1'

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

    def test_get_members_list(self):
        response = self.client.get(self.reverse(name='member-list'))
        self.response_403(response)

    def test_get_members_detail(self):
        response = self.client.get(self.reverse(name='member-detail', pk=1))
        self.response_403(response)

    def test_login_get_members_list(self):
        with self.login(username="kim", password="password"):
            response = self.client.get(self.reverse(name='member-list'))
            self.response_200(response)
