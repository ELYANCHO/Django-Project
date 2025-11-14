from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  favorite_game = models.CharField(null=True)
  playing_hours = models.IntegerField(null=True)
  game_gender = models.CharField(null=True)
