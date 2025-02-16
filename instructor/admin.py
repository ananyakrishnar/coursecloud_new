from django.contrib import admin

# Register your models here.
from instructor.models import User,Catagory,Course,Module
admin.site.register(User)
admin.site.register(Catagory)

class CourseAdmin(admin.ModelAdmin):
    exclude=("owner",)
    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner=request.user
        return super().save_model(request, obj, form, change)
    
admin.site.register(Course,CourseAdmin)
admin.site.register(Module)
