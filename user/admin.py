from django.contrib import admin
from user.models import User, UserLoginLog


class UserLoginLogAdmin(admin.ModelAdmin):
    '''
    log class to see log in admin homepage
    '''
    list_display = ('user', 'ip_address', 'user_agent')
    list_filter = ('ip_address',)
    date_hierarchy = 'created'


admin.site.register(User)
admin.site.register(UserLoginLog, UserLoginLogAdmin)
