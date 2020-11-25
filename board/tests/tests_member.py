from test_plus.test import TestCase, APITestCase
from rest_framework import status
from board.models import Post, Member



class MemberLogInAPITest(APITestCase):
    def setUp(self):
        self.user1 = self.make_user(username="Jhon", password="password")
        self.member1 = Member.objects.create(username="kim", name="kim", gender='M', tel="123456")
        self.member2 = Member.objects.create(username="jang", gender='W', tel="456789")
        self.post1 = Post.objects.create(title="DRF", description="how to learn DRF", writer=self.member1)
        self.post2 = Post.objects.create(title="Spring", description="how to learn Spring", writer=self.member2)

    def test_login(self):
        response = self.client.post(self.reverse('rest_framework:login'), data={ "username": "test1", "password": "123456!@#"})
        assert response.status_code == status.HTTP_200_OK
        #assert 'user' in response.data
        #assert response.data['user']['username'] == 'test1'

    def test_login_get_members_list(self):
        with self.login(username="Jhon", password="password"):
            response = self.client.get(self.reverse(name='member-list'))
            self.response_200(response)

    def test_login_put_members(self):
        with self.login(username="Jhon", password="password"):
            data = {
                "username": "Jae",
                "gender": "M",
                "tel": "0701577",
            }
            response = self.client.put('/board/member/1/', data=data)
            self.response_200(response)

    def test_login_delete_members(self):
        with self.login(username="Jhon", password="password"):
            response = self.client.delete('/board/member/1/')
            self.response_204(response)

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

    def test_logout_get_members_list(self):
        response = self.client.get(self.reverse(name='member-list'))
        self.response_403(response)

    def test_logout_get_members_detail(self):
        response = self.client.get(self.reverse(name='member-detail', pk=1))
        self.response_403(response)

    def test_logout_put_members(self):
        data = {
            "username": "Jae",
            "gender": "M",
            "tel": "0701577",
        }
        response = self.client.put('/board/member/1/', data=data)
        self.response_403(response)

    def test_logout_delete_members(self):
        response = self.client.delete('/board/member/1/')
        self.response_403(response)

    def test_str(self):
        with self.login(username="Jhon", password="password"):
            response = self.client.get('/board/member/2/')
            assert response.data['username'] == str(self.member1)