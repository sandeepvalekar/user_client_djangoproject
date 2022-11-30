from django.contrib import admin
from api.models import client,project,user
# Register your models here.

class UserAdmin(admin.ModelAdmin):
  list_display=('username','password','email')

class ClientAdmin(admin.ModelAdmin):
  list_display=('client_name','created_by','created_at')

class ProjectAdmin(admin.ModelAdmin):
  list_display=('project_name','client')

admin.site.register(client,ClientAdmin)
admin.site.register(project,ProjectAdmin)
admin.site.register(user,UserAdmin)