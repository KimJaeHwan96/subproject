from django.db import models
from django.contrib.auth.models import AbstractUser

GENDERS = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )


class Member(AbstractUser):
    name = models.CharField(max_length=10,)
    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS)
    birthday = models.DateField(verbose_name='생년월일')
    tel = models.CharField(verbose_name="연락처", max_length=20,)
    created_dt = models.DateTimeField(verbose_name="가입 일자", auto_now_add=True)
    updated_dt = models.DateTimeField(verbose_name="갱신 일자", auto_now=True)

    class Meta:
        db_table = 'member'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    writer = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='posts')
    created_dt = models.DateTimeField(verbose_name='작성 시간', auto_now_add=True)
    modify_dt = models.DateTimeField(verbose_name='변경 시간', auto_now=True)

    class Meta:
        ordering = ['modify_dt']

    def __str__(self):
        return self.title