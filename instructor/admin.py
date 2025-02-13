from django.contrib import admin

# Register your models here.
from instructor.models import User,Catagory,Course
admin.site.register(User)
admin.site.register(Catagory)
admin.site.register(Course)

