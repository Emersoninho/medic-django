from django.contrib import admin
from .models import Profile, Speciality, Dayweek, State, City, Neighborhood, Address,Rating

class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birthday',)
    empty_value_display = 'vazio'
    list_display_links = ('user', 'role',)
    list_filter = ('user__is_active', 'role')
    fields = ('user', ('role'), 'birthday', 'addresses',)
    exclude = ('favorites', 'created_at', 'update_at',)
    readonly_fields = ('user',)
    search_fields = ('user__username',)
    

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Speciality)
admin.site.register(Dayweek)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(Rating)