from django.contrib import admin

# Register your models here.
from instructor.models import User,Catagory
admin.site.register(User)
admin.site.register(Catagory)
