from django.contrib import admin
from feedback_app.models import Profile, Role, Structure, StructureUser, Level
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.site_header = 'Административная панель'


class StructureAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent', 'position')
    list_filter = ('level',)
    search_fields = ('name',)


admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Structure, StructureAdmin)
admin.site.register(StructureUser)
admin.site.register(Level)
