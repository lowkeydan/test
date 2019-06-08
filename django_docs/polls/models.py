from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='问题')
    pub_data = models.DateTimeField(verbose_name='发布时间')
    author = models.CharField(max_length=20, verbose_name='提问者', default='')
    email = models.EmailField(default='', max_length=20)
    def __str__(self):
        return self.question_text

class Person(models.Model):
    first_name =models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    def __str__(self):
        return self.first_name + self.last_name

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='该投票属于', null=True)
    choice_text = models.CharField(max_length=200, verbose_name='投票正文')
    votes = models.IntegerField(default=0, verbose_name='票数')
    voted_by = models.ForeignKey(Person, verbose_name='投给谁', default='',
                                 on_delete=models.CASCADE, null=True)
    url = models.URLField(default='www.example.com', blank='True')

    def __str__(self):
        return self.choice_text

class Person2(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person2,
        through='Membership',       ## 自定义中间表
        through_fields=('group', 'person'),
    )
    def __str__(self):
        return self.name

class Membership(models.Model):  # 这就是具体的中间表模型
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person2, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person2,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)
