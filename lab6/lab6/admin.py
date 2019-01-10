from django.contrib import admin

# Register your models here.

from lab7.models import Bullet

class BulletAdmin(admin.ModelAdmin):
    list_display = ('name','description','datetime','desc_len')
    list_filter = ['datetime']
    search_fields = ('id','name')
    
    def desc_len(self, obj):
        return len(obj.description)
    desc_len.short_description = "Длина сообщения"

admin.site.register(Bullet, BulletAdmin)
