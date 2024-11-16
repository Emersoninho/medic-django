from django.contrib import admin
from .models import Profile, Speciality, Dayweek, State, City, Neighborhood, Address,Rating

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialtiesList', 'addressesList',)

    class Media:
        css = {
            'all': ('css/custom.css',)
        }
        js = ('js/custom.js',)
    
    list_display = ('user', 'specialtiesList', 'addressesList',)

    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]
    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]
    
    list_display = ('user', 'birth',)

    def birth(self, obj):
        return obj.birthday
    birth.empty_value_display = '__/__/__'

    list_display = ('user', 'birth',)

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime('%d/%m/%Y')
        
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birthday',)
    empty_value_display = 'vazio'
    list_display_links = ('user', 'role',)
    list_filter = ('user__is_active', 'role')
    #fields = ('user', ('role'), 'image', 'birthday', 'specialties', 'addresses',)
    exclude = ('favorites', 'created_at', 'update_at',)
    readonly_fields = ('user',)
    search_fields = ('user__username',)
    fieldsets = (
        ('Usuário', {'fields': ('user', 'birthday', 'image',)}),
        ('Função', {'fields': ('role',)}),
        ('Extras', {'fields': ('specialties', 'addresses',)}),
    )

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Speciality)
admin.site.register(Dayweek)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(Rating)