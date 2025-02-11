from django.contrib import admin
from .models import User, Subject, Content, Activity

# Register your models here.
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Content)
admin.site.register(Activity)