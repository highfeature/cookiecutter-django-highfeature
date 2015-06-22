
from django.contrib import admin
from ..site.models.project import Project


class UserAdmin(admin.ModelAdmin):
    # ???
    #date_hierarchy = 'add_date'
    # field to display
    #fields = ('user_name', 'email',)
    # field to not display
    exclude = ('user_pw','unix_pw',)
    # field to display in the list
    list_display = ('id','user_name', 'realname',)

admin.site.register(Project)

