from django.db import models


class Question(models.Model):
    # 이렇게 정의되는 class가 데이터베이스의 Table과 mapping되요!
    # 그러면 Table의 column은 어떻게 정의해야 하나요? => 속성으로 표현
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
