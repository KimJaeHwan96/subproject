from test_plus.test import TestCase, APITestCase
from rest_framework import status
from board.models import Post, Member


class APITest(APITestCase):

    def setUp(self):
        self.user1 = self.make_user(username="Jhon", password="password")
        self.member1 = Member.objects.create(username="kim", gender='M', tel="123456")
        self.member2 = Member.objects.create(username="jang", gender='W', tel="456789")
        self.post1 = Post.objects.create(title="DRF", description="how to learn DRF", writer=self.member1)
        self.post2 = Post.objects.create(title="Spring", description="how to learn Spring", writer=self.member2)

    def test_login_get_posts_list(self):
        response = self.client.get(self.reverse(name='-list'))
        assert response.status_code == status.HTTP_200_OK

    def test_login_get_posts_detail(self):
        response = self.client.get(self.reverse(name='-detail', pk=1))
        self.response_200(response)

    def test_login_post_posts(self):
        with self.login(username="Jhon", password="password"):
            data = {
                "title": "JavaScript",
                "description": "Node.js, React.js, Vue.js",
                "writer": "2"
            }
            response = self.client.post('/board/', data=data)
            self.response_201(response)

    def test_login_put_posts(self):
        with self.login(username="Jhon", password="password"):
            data = {
                "title": "test2",
                "description": "Django Rest Framework",
                "writer": "2"
            }
            response = self.client.put('/board/2/', data=data)
            self.response_200(response)

    def test_login_delete_posts(self):
        with self.login(username="Jhon", password="password"):
            response = self.client.delete('/board/1/')
            self.response_204((response))


    def test_logout_get_posts_list(self):
        response = self.client.get('/board/')
        assert response.status_code == status.HTTP_200_OK

    def test_logout_get_posts_detail(self):
        response = self.client.get('/board/2/')
        self.response_200(response)

    def test_logout_post_posts(self):
        data = {
            "title": "JavaScript",
            "description": "Node.js, React.js, Vue.js",
            "writer": "2"
        }
        response = self.client.post('/board/', data=data)
        self.response_403(response)

    def test_logout_put_posts(self):
        data = {
            "title": "test2",
            "description": "Django Rest Framework",
            "writer": "2"
        }
        response = self.client.put('/board/2/', data=data)
        self.response_403(response)

    def test_logout_delete_posts(self):
        response = self.client.delete('/board/1/')
        self.response_403((response))

    def test_str(self):
        response = self.client.get('/board/1/')
        assert response.data['title'] == str(self.post1)