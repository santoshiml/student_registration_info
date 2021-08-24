from django.contrib import admin
from testapp.models import STUDENT
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['STUDENT_NAME', 'STUDENT_MARKS', 'STUDENT_DOB', 'STUDENT_DOJ']

# Register your models here.
admin.site.register(STUDENT, StudentAdmin)