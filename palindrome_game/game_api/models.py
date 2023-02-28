from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50,unique = True)
    password = models.CharField(max_length=50)

    class Meta:
        app_label = 'game_api'

class Game(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    game_id = models.CharField(max_length = 50, unique = True)
    board = models.CharField(max_length = 5 , default = " ")
    is_palindrome = models.BooleanField(default = False)

    class Meta:
        app_label = 'game_api'
