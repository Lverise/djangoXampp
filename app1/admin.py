from django.contrib import admin
from app1.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'fono', ]
# Register your models here.
admin.site.register(Employee,EmployeeAdmin)

