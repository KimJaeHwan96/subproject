from test_plus.test import TestCase, APITestCase
from rest_framework import status
from board.models import Post, Member, Comment


class CommentAPITest(APITestCase):
    def setUp(self):
        self.user1 = self.make_user(username="Jhon", password="password")
        self.member1 = Member.objects.create(username="kim", name="kim", gender='M', tel="123456")
        self.post1 = Post.objects.create(title="DRF", description="how to learn DRF", writer=self.member1)
        self.comment1 = Comment.objects.create(author=self.member1, post=self.post1, comment="Hi my name is KJH")
        self.comment2 = Comment.objects.create(author=self.member1, post=self.post1, comment="Hi my name is PSW")
        self.comment3 = Comment.objects.create(author=self.member1, post=self.post1, comment="Hi my name is LSW")

    def test_get_comment(self):
        response = self.client.get('/board/comment/')
        self.response_200(response)

    def test_get_post_comment(self):
        response = self.client.get('/board/post/1/get_comment/')
        self.response_200(response)

    def test_login_post_comment(self):
        with self.login(username="Jhon", password="password"):
            data = {
                "author": "1",
                "comment": "what are you doing?",
            }
            response = self.client.post('/board/comment/', data=data)
            self.response_201(response)

    def test_login_put_comment(self):
        with self.login(username="Jhon", password="password"):
            data = {
                "author": "1",
                "comment": "what are you doing?",
            }
            response = self.client.put('/board/comment/1/', data=data)
            self.response_200(response)

    def test_login_delete_comment(self):
        with self.login(username="Jhon", password="password"):
            response = self.client.delete('/board/comment/1/')
            self.response_204(response)

    def test_logout_post_comment(self):
        data = {
            "author" : "1",
            "comment" : "what are you doing?",
        }
        response = self.client.post('/board/comment/1/', data=data)
        self.response_403(response)

    def test_logout_put_comment(self):
        data = {
            "author": "1",
            "comment": "what are you doing?",
        }
        response = self.client.put('/board/comment/', data=data)
        self.response_403(response)

    def test_logout_delete_comment(self):
        response = self.client.delete('/board/comment/1/')
        self.response_403(response)

    def test_ordering_comment(self):
        response = self.client.get('/board/comment/?ordering=-1')
        comments = Comment.objects.all().order_by('-id')
        response_ids = [data['id'] for data in response.data['results']]
        comments_ids = list(comments.values_list('id', flat=True))
        assert response_ids == comments_ids
        self.response_200(response)