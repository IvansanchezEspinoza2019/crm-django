
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_organizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", null=True, blank=True, on_delete=models.SET_NULL)
    organization = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", related_name="leads",null=True, blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    name = models.CharField(max_length=20)
    organization = models.ForeignKey(UserProfileModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

def post_user_created_signal(sender, instance, created, **kwards):
    if created:
        UserProfileModel.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)