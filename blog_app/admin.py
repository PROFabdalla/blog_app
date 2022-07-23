import imp
from django.contrib import admin
from blog_app.models import category,post,comment
# Register your models here.


admin.site.register(category)
admin.site.register(post)
admin.site.register(comment)
admin.site.site_header='WELCOME to Information Technology Institute'
admin.site.site_title='iti'
admin.site.index_title = 'WELCOME ADMIN USER TO Information Technology Institute'

admin.register = 'wlcome'


