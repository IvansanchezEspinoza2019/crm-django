from django.contrib import admin

# Register your models here.
from .models import User, Lead, Agent, UserProfileModel

admin.site.register(User)

admin.site.register(UserProfileModel)
admin.site.register(Lead)

admin.site.register(Agent)