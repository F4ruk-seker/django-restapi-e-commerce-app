from django.db import models
from django.contrib.auth.models import User


class QuestionModel(models.Model):
    class StatusType(models.TextChoices):
        HIDE = 'H', 'HIDE'
        SHOW = 'S', 'SHOW'
        WAITING = 'W', 'WAITING'
        ANSWERED = 'A', 'ANSWERED'
        ANSWER_RATED = 'R', 'ANSWER_RATED'

    product = models.ForeignKey('products.ProductModel', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    question = models.CharField(max_length=500, blank=True)
    answer = models.CharField(max_length=500, blank=True)
    is_answer_helpus = models.NullBooleanField(default=None)
    ip = models.CharField(max_length=15, blank=True)
    status = models.CharField(max_length=10, choices=StatusType, default=StatusType.SHOW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public_question = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
