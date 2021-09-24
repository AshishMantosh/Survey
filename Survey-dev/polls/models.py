from django.db import models


class Question(models.Model):
    question_text = models.CharField('Question', max_length=500)
    created_at = models.DateTimeField('Published Date', auto_now_add=True)
    modified_at = models.DateTimeField('Last Modified', auto_now=True)

    def __str__(self):
        return self.question_text


class Option(models.Model):
    option_text = models.CharField('Option', max_length=500)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.option_text